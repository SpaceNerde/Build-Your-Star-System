# sol.py
# Author: Florian Pospiech


# Example of use

from solar import SolarSystem, SolarSystemObject

solar_system = SolarSystem(400)

body = SolarSystemObject(solar_system, 100, velocity=(1, 1, 1))

for _ in range(100):
    solar_system.update_all()
    solar_system.draw_all()


