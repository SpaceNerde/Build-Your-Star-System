# vectors.py
# Author: Florian Pospiech

# Class to Create and edit Vectors... because I'm lazy.... :D
class Vector:
    # Define Vector
    def __init__(self, x=0, y=0, z=0):
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