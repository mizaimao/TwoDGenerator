import numpy as np
import cv2
from objs.stage import Stage

# color in BGR 
color_dict = {'blue': (245, 158, 66), 'red': (95, 95, 250)}

class Renderer:
    def __init__(self, init_stage: Stage):
        self.current_stage = init_stage
