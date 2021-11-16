import random
import numpy as np
from typing import List, Tuple, no_type_check
from functools import reduce
from enum import Enum
from utils.math_utils import TransformationMatrix, calculate_object_center, get_transformation_matrix_from_enum, TransformationType


class WireframeStructure():
    def __init__(self, coordinates: list, struct_index: int) -> None:
        self.coordinates = coordinates
        self.vertices = len(self.coordinates)

        self.homogeneous_coordinates = self.get_homogeneous_coordinates()
        self.center = Tuple[float, float]

        # List[int] represents the parameters of a transformation, ex: rotation point, rotation degree, etc
        self.transformation_info: List[Tuple[TransformationType, List[int]]] = []
        # List of matrix transformations
        self.transformations: List[list] = []
        self.transformed_coordinates: List = []
        self.transformed_points: List = []

        self.struct_type = WireframeType(self.vertices).name
        self.struct_name = f"{self.struct_type}_{struct_index}"
        self.color = WireframeColor(random.randrange(1, 7)).name # TODO update to selected color

        self.transform_to_points()


    def get_homogeneous_coordinates(self) -> np.ndarray:
        aux_matrix = np.ones((len(self.coordinates), 1))
        return np.hstack((self.coordinates, aux_matrix))

    def calculate_object_center(self) -> None:
        self.center = tuple(np.array(self.transformed_coordinates).mean(axis=0))


    def transform_to_points(self) -> None:
        self.transformations = []
        for (transform_type, params) in self.transformation_info:
            self.transformations.append(get_transformation_matrix_from_enum(transform_type)(*params))

        self.transformed_points = []
        acc = []
        for c in self.homogeneous_coordinates:
            transformed_c = reduce(np.dot, [c, *self.transformations])
            acc.append((transformed_c[0], transformed_c[1]))
        self.transformed_coordinates = acc

    def transform(self) -> None:
        coordinates = self.get_homogeneous_coordinates()
        for (transform_type, params) in self.transformation_info:
            accum_translation:list = []
            if transform_type is TransformationType.ROTATION or transform_type is TransformationType.SCALING:
                if transform_type is TransformationType.ROTATION:
                    rotate_around_origin = len(params) == 2
                    if rotate_around_origin:
                        t_x, t_y = params[1]
                    else:
                        t_x, t_y, _ = calculate_object_center(coordinates)
                    params = [params[0]]
                else:
                    t_x, t_y, _ = calculate_object_center(coordinates)
                first_tr_matrix = TransformationMatrix.translation(-t_x, -t_y)
                transform_matrix = get_transformation_matrix_from_enum(transform_type)(*params)
                second_tr_matrix = TransformationMatrix.translation(t_x, t_y)
                accum_translation.append([first_tr_matrix, transform_matrix, second_tr_matrix])
            else:
                operation_matrix = get_transformation_matrix_from_enum(transform_type)
                accum_translation.append(operation_matrix(*params))

            transformed_points = []
            for point in coordinates:
                transformed_points.append(tuple(reduce(np.dot, [point, *accum_translation])))
            coordinates = np.array(transformed_points)

        # Recalculate center after translations
        self.center = calculate_object_center(coordinates)

        # Remove last coordinate
        aux = coordinates[:, :-1]
        self.transformed_coordinates = tuple(map(lambda x : (x[1][0], x[1][1]), aux))
        return


class WireframeType(Enum):
    """ The Structure type is defined by how many coordinates it has.
        The Polygon type is accessed if the amount cannot be found,
        using the Enum class method '_missing_'
    """
    INVALID = 0
    POINT = 1
    LINE = 2
    POLYGON = -1

    @classmethod
    @no_type_check
    def _missing_(cls, value):
        return WireframeType.POLYGON

class WireframeColor(Enum):
    """Uses PyQt5.QtCore.Qt colors"""
    white = 1
    red = 2
    green = 3
    cyan = 4
    magenta = 5
    yellow = 6
