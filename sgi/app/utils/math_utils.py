# Math
import numpy as np


class Matrix():
    def __init__(self, angle: float, Dx: float, Dy: float, Sx: float, Sy: float) -> None:
        self.angle = angle
        self.Dx = Dx
        self.Dy = Dy
        self.Sx = Sx
        self.Sy = Sy

    def rotation (self) -> list:
        rotation_matrix = np.identity(3)
        angle = np.radians(self.angle)

        rotation_matrix[0][0] = np.cos(angle)
        rotation_matrix[0][1] = -1 * np.sin(angle)
        rotation_matrix[1][0] = np.sin(angle)
        rotation_matrix[1][1] = np.cos(angle)

        return rotation_matrix


    def translation(self) -> list:
        translation_matrix = np.identity(3)
        translation_matrix[2][0] = self.Dx
        translation_matrix[2][1] = self.Dy

        return translation_matrix

    def scaling(self) -> list:
        scaling_matrix = np.identity(3)
        scaling_matrix[0][0] = self.Sx
        scaling_matrix[1][1] = self.Sy

        return scaling_matrix
