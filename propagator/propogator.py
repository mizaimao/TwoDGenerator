import numpy as np
from objs.stage import Stage
from objs.obj_collector import ObjectCollector
from timers.button_timer import ButtonTimer

def update_by_button_timer(stage: Stage,
                        obj_collector: ObjectCollector,
                        timer: ButtonTimer,):
    update_stage_by_timer(stage, timer)
    update_objects_by_timer(obj_collector, timer)


def update_stage_by_timer(stage: Stage, timer: ButtonTimer):
    return
    
def update_objects_by_timer(obj_collector: ObjectCollector,
                            timer: ButtonTimer):
    for dot in obj_collector.dot_collector:
        print(dot.position)
        dot.update_location(delta_time = timer.delta_time)

    return
