import pygame
import math

# ------- CONFIGURATION AND CONSTANTS -------
pygame.init()

# Screen dimensions
WIDTH : int = 800
HEIGHT: int = 600

# Initialize display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect Simulation")

# ------- SIMULATION CONSTANTS -------
PLANET_MASS = 100         # Mass of the planet (arbitrary units)
SPACECRAFT_MASS = 5       # Mass of the spacecraft (arbitrary units)
G = 5                     # Gravitational constant (tuned for visual scaling)
PLANET_RADIUS = 50        # Radius of the planet (in pixels)
SPACECRAFT_SIZE = 5       # Radius of the spacecraft (circular shape used for simulation)
VEL_SCALE = 100           # Scaling factor for initial launch velocity
FPS = 60                  # Frames per second (simulation speed)

# Load images and background
BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH,HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("jupiter.png"), (PLANET_RADIUS * 2, PLANET_RADIUS * 2))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ------- CLASS DEFINITIONS -------
class Planet:
    """Represents a stationary planet exerting gravitational force."""

    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        """Draw the planet centered on its position."""
        screen.blit(PLANET, (self.x - PLANET_RADIUS, self.y - PLANET_RADIUS))

class Spacecraft:
    """Represents a spacecraft influenced by the planet's gravity."""

    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def move(self, planet = None):
        """
        Update spacecraft position under gravitational influence.
        Uses Newton's Law of Gravitation:
            F = G * (m1 * m2) / r^2
        Acceleration = F / m1
        """
        # Compute distance from planet
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        
        # Avoid division by zero
        if distance == 0:
            return
        
        # Gravitational force magnitude
        force = (G * self.mass * planet.mass) / distance**2
        
        # Acceleration magnitude
        acceleration = force / self.mass

        # Direction (angle) toward planet
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        # Resolve acceleration into components
        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        # Update velocity and position
        self.vel_x += acceleration_x
        self.vel_y += acceleration_y
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self):
        """Draw the spacecraft as a small red circle."""
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), SPACECRAFT_SIZE)

# ------- HELPER FUNCTIONS -------
def create_ship(location, mouse):
    """
    Create a spacecraft with initial velocity based on drag direction.
    The line drawn by the user determines the launch vector.
    """
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    spacecraft = Spacecraft(t_x, t_y, vel_x, vel_y, SPACECRAFT_MASS)
    return spacecraft

# ------- MAIN FUNCTION -------
def main():
    """Main loop handling simulation, rendering, and user input."""
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    spacecrafts = []            # List of active spacecrafts
    temp_obj_pos = None         # Temporary variable for launch setup
    
    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse click logic: first sets start position, second sets velocity
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    spacecraft = create_ship(temp_obj_pos, mouse_pos)
                    spacecrafts.append(spacecraft)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        screen.blit(BG, (0,0))

        # Draw velocity preview line
        if temp_obj_pos:
            pygame.draw.line(screen, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(screen, RED, temp_obj_pos, SPACECRAFT_SIZE)

        # Update and draw spacecrafts
        for spacecraft in spacecrafts[:]:
            spacecraft.draw() 
            spacecraft.move(planet)

            # Remove spacecraft if it goes off-screen or collides
            off_screen = spacecraft.x < 0 or spacecraft.x > WIDTH or spacecraft.y < 0 or spacecraft.y > HEIGHT
            collided = math.sqrt((spacecraft.x - planet.x)**2 + (spacecraft.y - planet.y)**2) <= PLANET_RADIUS
            if off_screen or collided:
                spacecrafts.remove(spacecraft)  

        # Draw planet
        planet.draw()

        # Update display
        pygame.display.update()

    pygame.quit()

# -------- Entry Point -------
if __name__ == "__main__":
    main()
