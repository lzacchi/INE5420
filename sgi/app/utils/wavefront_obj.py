"""Wavefront.obj File handler"""

from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from wireframe_structure import WireframeStructure
from enum import Enum, auto
from typing import List, Dict, Union
from pathlib import Path


WHITE = QColor(255, 255, 255)

class ObjHeader(Enum):
    MTLLIB = "mtllib"
    USEMTL = "usemtl"
    OBJ_NAME = "o"
    VERTICE = "v"
    POINT = "p"
    LINE = "l"
    FACE = "f"
    # W = auto() ?

    def __str__(self) -> str:
        return super().__str__()


class ObjReader:
    def __init__(
            self,
            filepath: str,
            index: int,
            normalization_values: list,
            transformations: list
        ) -> None:
        self.filepath = filepath
        self.wireframes: list = []
        self.index = index
        self.normalization_value = normalization_values
        self.transformations = transformations

        self.parse_functions = {
            ObjHeader.MTLLIB.value: self.parse_mttlib,
            ObjHeader.USEMTL.value: self.parse_usemtl,
            ObjHeader.OBJ_NAME.value: self.parse_obj_name,
            ObjHeader.VERTICE.value: self.parse_vertice,
            # ObjHeader.POINT.value: self.parse_elements, # w
            ObjHeader.POINT.value: self.parse_elements,
            ObjHeader.LINE.value: self.parse_elements,
            ObjHeader.FACE.value: self.parse_elements,
        }
        self.material_parser = {"newmtl": self.parse_newmtl, "Kd": self.parse_Kd}

        self.material: QColor = WHITE
        self.material_table: dict = {}
        self.material_str = ""
        self.obj_str = ""
        self.vertices: list = []

        self.load_obj(filepath)

    def __str__(self) -> str:
        return ""

    def parse_mttlib(self, params:list) -> None:
        filename = params[0]
        self.split_and_parse_file(str(Path().absolute()/ "resources" / "obj" / filename), self.material_parser)

    def parse_usemtl(self, params:list) -> None:
        material_file = params[0]
        self.material = self.material_table[material_file]

    def parse_obj_name(self, params:list) -> None:
        self.obj_str = params[0]

    def parse_vertice(self, params: list) -> None:
        x, y = params
        self.vertices.append((float(x), float(y)))

    def parse_elements(self, params:list) -> None:
        points = []
        for v in params:
            if v[0] == "-":
                index = int(v)
            else:
                index = int(v) -1
            points.append(self.vertices[index])
        
        no_color = not self.material
        if no_color:
            self.material = WHITE
        wireframe = WireframeStructure(
            points, self.index, self.material, self.normalization_value, self.transformations, self.obj_str
        )
        self.wireframes.append(wireframe)
        
        # Clear variables and increment index
        self.material = WHITE
        self.obj_str = ""
        self.index += 1

    def parse_newmtl(self, params: list) -> None:
        self.material_str = params[0]

    def parse_Kd(self, params: list) -> None:
        color = QColor(
            int(params[0] * 255),
            int(params[1] * 255),
            int(params[2] * 255),
        )
        self.material_table[self.material_str] = color
        self.material_str = ""

    def load_obj(self, filepath: str) -> None:
        # split and parse with default parser
        self.split_and_parse_file(filepath, self.parse_functions)

    def split_and_parse_file(self, filepath: str, parser: Dict) -> None:
        with open(filepath) as f:
            for line in f.readlines():
                l = line.strip().split()
                try:
                    header = l[0] # Header should match the value in our ObjHeader enum
                    params = l[1:]
                    parser[header](self, params)
                except Exception as e:
                    print(e)
                    continue


class ObjWriter:
    # TODO dar uma melhorada nessa api aqui
    def __init__(self, scene_name: List[str], wireframes: list) -> None:
        self.scene_name: list = []
        self.wireframes: list = []

    def __str__(self) -> str:
        return f"{self.scene_name}"

    def write_obj(self) -> None:
        pass

    def save_file(self, filename: str, lines: List[str]) -> None:
        with open(filename, "w") as writer:
            for line in lines:
                writer.write(line)
