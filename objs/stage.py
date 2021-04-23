"""
"Background" of current frame.
"""
import numpy as np

class Stage:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.array = np.full((self.width, self.height))