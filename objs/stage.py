"""
"Background" of current frame.
"""
import numpy as np

class Stage:
    def __init__(self, from_array: np.array = None, width: int = -1, height: int = -1):
        if from_array is not None:
            self.array = from_array
            self.width = from_array.shape[0]
            self.height = from_array.shape[1]
        else:
            assert width > 0 and height > 0
            self.width = width
            self.height = height
            self.array = np.full((self.height, self.width, 3), 255)