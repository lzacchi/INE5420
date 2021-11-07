def x_viewport(x_window: float,
         xwindow_min: float,
         xwindow_max: float,
         xvp_min: float,
         xvp_max: float) -> float:

    """Return the x coordinate of the viewport transformation function"""
    x_vp = ((x_window - xwindow_min)/xwindow_max - xwindow_min) * (xvp_max - xvp_min)
    return x_vp

def y_viewport(y_window: float,
               ywindow_min: float,
               ywindow_max: float,
               yvp_min: float,
               yvp_max: float) -> float:
    """Return the y coordinate of the viewport transformation function"""

    y_vp = (1 - ((y_window - ywindow_min)/ywindow_max - ywindow_min)) * (yvp_max - yvp_min)
    return y_vp