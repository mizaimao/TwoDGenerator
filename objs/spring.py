"""
Spring model controlled by Hooke's law.
"""

class Spring:
    def __init__(self, stiffness: float, rest_length: float, damping_factor: float):
        self.stiffness = stiffness
        self.rest_length = rest_length
        self.damping_factor = damping_factor
        