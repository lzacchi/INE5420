def x_viewport(x_window: int,
         xwindow_min: int,
         xwindow_max: int,
         xvp_min: int,
         xvp_max: int) -> float:

    """Return the x coordinate of the viewport transformation function"""
    x_vp = (x_window - xwindow_min/xwindow_max - xwindow_min) * (xvp_max - xvp_min)
    return x_vp

def y_viewprot(y_window: int,
               ywindow_min: int,
               ywindow_max: int,
               yvp_min: int,
               yvp_max: int) -> float:
    """Return the y coordinate of the viewport transformation function"""

    y_vp = (1 - (y_window - ywindow_min/ywindow_max - ywindow_min)) * (yvp_max - yvp_min)
    return y_vp
