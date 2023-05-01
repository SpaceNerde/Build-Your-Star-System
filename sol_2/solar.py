# solar.py
# Author: Florian Pospiech

import matplotlib.pyplot as plt

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