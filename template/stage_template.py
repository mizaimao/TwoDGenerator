"""
Interface to load stage template from image files.
"""
import cv2

from objs.stage import Stage

def load_template_stage(image_name: str) -> Stage:
    """
    Load the given image path and return Stage object.

    Arguments
        image_name -- path to image to be loaded

    Returns
        Stage -- loaded image as stage object

    Raises
        ValueError -- image incompatible 

    """
    stage_image = cv2.imread(image_name)

    # single channel image
    image_ndim = stage_image.ndim
    if image_ndim == 2:
        stage_image = cv2.cvtColor(stage_image, cv2.COLOR_GRAY2RGB)
    elif image_ndim == 3:
        #pass
        stage_image = cv2.cvtColor(stage_image, cv2.COLOR_RGB2BGR)
    else:
        raise ValueError("%d channel image incompatible." % image_ndim)
    
    return Stage(from_array = stage_image)
