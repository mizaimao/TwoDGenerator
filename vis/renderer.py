import numpy as np
import cv2
from objs.stage import Stage
from objs.obj_collector import ObjectCollector

# color in BGR 
color_dict = {'blue': (245, 158, 66), 'red': (95, 95, 250)}

class Renderer:
    def __init__(self, init_stage: Stage):
        self.current_stage = init_stage
        self.current_frame = None
        self.objs = []

    def update_frame(self, object_collector: ObjectCollector):
        self.draw_objects(self.current_stage, object_collector)
        
        return self.current_frame

    def draw_objects(self, stage: Stage, object_collector: ObjectCollector):
        frame = stage.array.copy().astype(np.uint8)
        for dot in object_collector.dot_collector:

            frame = cv2.circle(frame,
                      center = dot.position,
                      radius = dot.radius,
                      color = (150, 0, 150),
                      thickness = 2,
                      lineType = cv2.LINE_8,
                      shift = 0 
                      )

        self.current_frame = frame
