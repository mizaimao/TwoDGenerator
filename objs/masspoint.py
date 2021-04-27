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

        self.ve_acc = 0.0  # vertical
        self.ho_acc = 40   # horizontal

        self.ve_spd = 120.0
        self.ho_spd = 0.0

    def update_speed(self, delta_time: float):
        self.ve_spd = self.ve_spd + self.ve_acc * delta_time
        self.ho_spd = self.ho_spd + self.ho_acc * delta_time

    def update_acceleration(self, delta_time: float):
        self.ve_acc = 10.0
        self.ho_acc = 9.8 

    def update_location(self, delta_time: float):
        new_x = self.position[0] + self.ve_spd * delta_time + (1 / 2) * self.ve_acc * (delta_time ** 2)
        new_y = self.position[1] + self.ho_spd * delta_time + (1 / 2) * self.ho_acc * (delta_time ** 2)

        self.update_speed(delta_time)
        self.position = (int(new_x), int(new_y))
        print((1 / 2) * self.ve_acc * (delta_time ** 2), (1 / 2) * self.ho_acc * (delta_time ** 2))

    """
    TODO: collision detection
    def ray_casting(self, ray_length: float = 20.0):
    """