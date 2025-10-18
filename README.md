# 🌌 Gravitational Slingshot Simulator

A Python + Pygame simulation that visually demonstrates the **gravitational slingshot effect**, a technique used by spacecraft to gain speed and change trajectory using the gravity of a planet.

---

## 🚀 Features
- Realistic gravity-based motion using **Newton’s Law of Gravitation**  
- Interactive **launch control:** click and drag to set spacecraft direction and velocity  
- Smooth visuals with adjustable constants for **mass**, **gravity**, and **velocity scaling**  
- Automatic handling of **collisions** and **off-screen** objects  

---


## 🕹️ Controls
| Action | Description |
|--------|--------------|
| **Left Click (1st time)** | Set spacecraft launch position |
| **Left Click (2nd time)** | Set launch direction and velocity (drag from start to release) |
| **Quit** | Press the window close button |

---

## ⚙️ Configuration
You can adjust physical and visual constants in the code section:
```python
PLANET_MASS = 100          # Mass of the planet
SPACECRAFT_MASS = 5        # Mass of the spacecraft
G = 5                      # Gravitational constant (tuned for scaling)
PLANET_RADIUS = 50         # Radius of the planet (pixels)
SPACECRAFT_SIZE = 5        # Radius of the spacecraft (pixels)
VEL_SCALE = 100            # Launch velocity scaling
FPS = 60                   # Simulation frame rate
```
---

## 🛠 Installation & Run

### Prerequisites
- **Python 3.8+** installed on your system.
- **pip** (Python package manager).
- Python libraries:
  - `pygame`
  - `math` 

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/NJ-DEV-616/gravitational-slingshot-simulator.git
   cd gravitational-slingshot-simulator
2. **Install Dependencies**
    ```bash
    pip install pygame
3. **Run the Program**
    ```bash
    python main.py
---
## 🧾 License
This project is licensed under the [MIT License](LICENSE).
---
