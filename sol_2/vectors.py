# vectors.py
# Author: Florian Pospiech

import math

# Class to Create and edit Vectors... because I'm lazy.... :D
class Vector:
    # Define Vector
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # repr output
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Default Sting output
    def __str__(self):
        return f"{self.x}a + {self.y}b + {self.z}c"

    # make Vector Indexable
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item ==2:
            return  self.z
        else:
            return TypeError("There only 3 vectors")

    # Addition of 2 Vectors
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # Subtraction of 2 Vectors
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    # Multiplication and Scala of Vectors
    def __mul__(self, other):
        if isinstance(other, Vector):
            return (
                self.x * other.x +
                self.y * other.y +
                self.z * other.z
            )
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            TypeError("operand hsa to be a Vector, int or float... pls")

    # basic Division of Vectors
    def __truediv__(self, other):
        return Vector(
            self.x / other,
            self.y / other,
            self.z / other,
        )

    # Get The Magnitude of a Vector... this comment is properly really useless...
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Normalization of Vector
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )