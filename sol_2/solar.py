# solar.py
# Author: Florian Pospiech

import math
import matplotlib.pyplot as plt

from vectors import Vector


# to lazy to comment all of this out...
class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.objects = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize = (self.size / 50, self.size / 50)
        )
        self.fig.tight_layout()

    def add_object(self, object):
        self.objects.append(object)

    def update_all(self):
        for object in self.objects:
            object.move()
            object.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.ax.clear()

class SolarSystemObject:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(self, solar_system, mass, position=(0,0,0), velocity=(0,0,0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size
        )
        self.colour = "black"

        self.solar_system.add_object(self)

    # make that shit move!!!!
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2]
        )

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker = "o",
            markersize = self.display_size,
            color = self.colour
        )