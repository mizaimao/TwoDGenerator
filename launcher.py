#!/usr/bin/env python3
import cv2
import sys
import os
import time
import numpy as np

from vis.renderer import Renderer
from objs.masspoint import MP
from objs.stage import Stage
from objs.spring import Spring
from timers.button_timer import ButtonTimer
from objs.obj_collector import ObjectCollector
from propagator.propogator import update_by_button_timer
from template.stage_template import load_template_stage

WINDOW_NAME = "Chicken Stage"
WIDTH = 1920
HEIGHT = 1080

def update_by_frame():
    frame_counter = 0
    #stage = Stage(width = WIDTH, height = HEIGHT)
    stage = load_template_stage('/Users/frank/Projects/TwoDGenerator/template/debug_stage0.png')
    renderer = Renderer(init_stage = stage)
    timer = ButtonTimer(frames_per_second = 24)

    # first mass point
    mp0 = MP(id = 0, mass = 10, radius = 10, position = (500, 200))
    mp1 = MP(id = 1, mass = 10, radius = 10, position = (500, 400))  
    oc = ObjectCollector()
    oc.dot_collector.extend([mp0, mp1])

    k = ord('n')
    while k == ord('n'):
        frame_counter += 1

        update_by_button_timer(stage, oc, timer)

        single_frame = renderer.update_frame(oc)
        cv2.imshow(WINDOW_NAME, single_frame) 
        k = cv2.waitKey(0)
        cv2.destroyAllWindows()
    return


if __name__ == '__main__':
    update_by_frame()    
