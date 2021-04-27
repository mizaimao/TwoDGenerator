"""
"Background" of current frame.
"""
import numpy as np

class Stage:
    """
    Attributes
        display_array: image array to be displayed as a picture
        array: internal hidden array handeling collision and stuffs
        width/height: self-explanatory
    """
    def __init__(self, from_array: np.array = None, width: int = -1, height: int = -1):
        """
        Arguments
            from_array: input image array, to be processed as interal collision map
            width/height: defines sizes of array and collision map
        """
        if from_array is not None:
            self.display_array = from_array
            self.array = from_array
            #self.array = np.mean(from_array, axis = 2)
            print(from_array[300, 500])
            self.width = from_array.shape[1]
            self.height = from_array.shape[0]

        else:
            assert width > 0 and height > 0
            self.width = width
            self.height = height
            self.array = np.full((self.height, self.width, 3), 255)
            self.from_array = np.full((self.height, self.width, 3), 255)