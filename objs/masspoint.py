"""
Mass point as building blocks of bigger object (I guess).
"""

class MP:
    def __init__(self,
                 id: int,
                 mass: float,
                 radius: float,
                 position: (float, float)
                ):
        self.id = id
        self.mass = mass
        self.radius = radius
        self.position = position
