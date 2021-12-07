import random
import numpy as np

from typing import List, Tuple, no_type_check
from functools import reduce
from enum import Enum
from PyQt5.QtGui import QColor
from utils.coordinates import Coordinates
from utils.math_utils import (
    TransformationMatrix,
    calculate_object_center,
    get_transformation_matrix_from_enum,
    normalize_coordinate,
    TransformationType)
from utils.obj_header import ObjHeader


def get_homogeneous_coordinates(coordinates:list) -> np.ndarray:
    aux_matrix = np.ones((len(coordinates), 1))
    return np.hstack((coordinates, aux_matrix))

class WireframeStructure():
    def __init__(self, coordinates: list, struct_index: int, color: QColor, normalization_params:Coordinates , window_transformations: list) -> None:
        self.coordinates = coordinates
        self.vertices = len(self.coordinates)

        self.visibility = True
        self.fill = False

        self.homogeneous_coordinates = get_homogeneous_coordinates(self.coordinates)
        self.center: Tuple[float, float] = (0.0, 0.0)

        # List[int] represents the parameters of a transformation, ex: rotation point, rotation degree, etc
        self.transformation_info: List[Tuple[TransformationType, List[int]]] = []
        # List of matrix transformations
        self.transformations: List[list] = []
        self.transformed_coordinates: List = []
        self.transformed_points: List = []

        self.normalization_params = normalization_params
        self.window_transformations = window_transformations
        self.window_width = self.normalization_params.max_x - self.normalization_params.min_x
        self.window_height = self.normalization_params.max_y - self.normalization_params.min_y

        self.struct_type = WireframeType(self.vertices).name
        self.struct_name = f"{self.struct_type}_{struct_index}"
        self.color = color

        self.transform_to_points()
        self.transform()

    def set_name(self, name: str) -> None:
        self.name = name

    def get_dimension(self) -> int:
        return len(self.coordinates)

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
        coordinates = get_homogeneous_coordinates(self.coordinates)
        coordinates = np.dot(coordinates, self.window_transformations)

        for (transform_type, params) in self.transformation_info:
            accum_translation:list = []
            if transform_type is TransformationType.ROTATION or transform_type is TransformationType.SCALING:
                if transform_type is TransformationType.ROTATION:
                    rotate_around_origin = len(params) == 2 and params[1] is not None
                    if rotate_around_origin:
                        t_x, t_y = normalize_coordinate(params[1], self.window_height, self.window_width)
                    else:
                        # When the second param is empty we need to calculate the coordinates center
                        t_x, t_y, _ = calculate_object_center(coordinates)
                    params = [params[0]] # remove extra params
                else:
                    t_x, t_y, _ = calculate_object_center(coordinates)
                first_tr_matrix = TransformationMatrix.translation(-t_x, -t_y)
                transform_matrix = get_transformation_matrix_from_enum(transform_type)(*params)
                second_tr_matrix = TransformationMatrix.translation(t_x, t_y)
                accum_translation += [first_tr_matrix, transform_matrix, second_tr_matrix]
            else:
                if transform_type is TransformationType.TRANSLATION:
                    x, y = normalize_coordinate(params, self.window_height/2, self.window_width/2)
                    params = [x, y]
                operation_matrix = get_transformation_matrix_from_enum(transform_type)
                accum_translation.append(operation_matrix(*params))

            transformed_points = []
            for point in coordinates:
                reduced = tuple(reduce(np.dot, [point, *accum_translation]))
                transformed_points.append(reduced)
            coordinates = np.array(transformed_points)

        # Recalculate center after translations
        self.center = calculate_object_center(coordinates)

        # Remove last coordinate
        aux = coordinates[:, :-1]
        self.transformed_coordinates = list(map(lambda x : tuple(x), aux))
        return # breakpoint for testing


    def to_obj_str(self, denormalization_matrix: list) -> Tuple[List[str], List[str]]:
        coordinates = get_homogeneous_coordinates(self.transformed_coordinates)
        denormalizated_coordinates = np.dot(coordinates, denormalization_matrix)

        # Write file headers
        obj_info = [
            f"{ObjHeader.OBJ_NAME.value} {self.name}",
            f"{ObjHeader.USEMTL.value} {self.name}_mtl", # material files must always end their name with '_mtl'
        ]
        list(map(lambda v: obj_info.append(f"{ObjHeader.VERTICE.value} {v[0]} {v[1]} 0.0"), denormalizated_coordinates))

        # Gather point info
        points = ["-" + str(n+1) for n in range(self.get_dimension())]
        points.reverse() # First defined points first
        line = [ObjHeader.FACE.value]
        line.extend(points)
        points_line = " ".join(line)
        obj_info.append(points_line)

        # Make material info
        r, g, b, a = self.color.getRgb()
        material_info = [
            f"{ObjHeader.NEWMTL.value} {self.name}_mtl",
            f"{ObjHeader.KD.value} {r/255} {g/255} {b/255} {a/255}"
        ]

        return (
            list(map(lambda x: x + "\n", obj_info)),
            list(map(lambda x: x + "\n", material_info)),
        )


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
