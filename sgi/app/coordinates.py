class Coordinates():
    def __init__(self, min_x: float, min_y: float, max_x: float, max_y: float, factor: float) -> None:
        self.min_x = min_x
        self.min_y = min_y

        self.max_x = max_x
        self.max_y = max_y

        self.factor = factor
