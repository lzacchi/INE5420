# Math

import numpy as np
from enum import Enum
from typing import no_type_check, Any
from functools import reduce


class TransformationType(Enum):
    ROTATION = 0
    TRANSLATION = 1
    SCALING = 2


def get_transformation_matrix_from_enum(e: TransformationType) -> Any:
    if e is TransformationType.ROTATION:
        return TransformationMatrix.rotation
    elif e is TransformationType.TRANSLATION:
        return TransformationMatrix.translation
    else:
        return TransformationMatrix.scaling


def calculate_object_center(coordinates: np.ndarray) -> tuple:
    center_coordinates = coordinates.mean(axis=0) # compute the mean of the coord array
    tuple_coordinates = tuple(center_coordinates)
    return tuple_coordinates


def normalize_window(x_shift:float, y_shift:float, width: float, height: float, angle:float) -> list:
    rotation_matrix = TransformationMatrix.rotation(angle)
    translation_matrix = TransformationMatrix.translation(x_shift, y_shift)
    scaling_matrix = TransformationMatrix.scaling(2/width, 2/height)

    normalization = reduce(np.dot, [translation_matrix, rotation_matrix, scaling_matrix])
    
    return normalization

class TransformationMatrix():
    @staticmethod
    @no_type_check
    def rotation(angle:float) -> list:
        rotation_matrix = np.identity(3)
        angle = np.radians(angle)

        rotation_matrix[0][0] = np.cos(angle)
        rotation_matrix[0][1] = -1 * np.sin(angle)
        rotation_matrix[1][0] = np.sin(angle)
        rotation_matrix[1][1] = np.cos(angle)

        return rotation_matrix

    @staticmethod
    @no_type_check
    def translation(dx: float, dy: float) -> list:
        translation_matrix = np.identity(3)
        translation_matrix[2][0] = dx
        translation_matrix[2][1] = dy

        return translation_matrix

    @staticmethod
    @no_type_check
    def scaling(sx: float, sy: float) -> list:
        scaling_matrix = np.identity(3)
        scaling_matrix[0][0] = sx
        scaling_matrix[1][1] = sy

        return scaling_matrix
