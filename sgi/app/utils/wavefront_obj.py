"""Wavefront.obj File handler"""

from wireframe_structure import WireframeStructure
from enum import Enum, auto
from typing import List, Dict
from pathlib import Path


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
        self.index = index
        self.normalization_value = normalization_values
        self.transformations = transformations

        self.parse_functions = {
            ObjHeader.MTLLIB.value: self.parse_mttlib,
            ObjHeader.USEMTL.value: self.parse_usemtl,
            ObjHeader.OBJ_NAME.value: self.parse_obj_name,
            ObjHeader.VERTICE.value: self.parse_point,
            ObjHeader.POINT.value: self.parse_point,
            ObjHeader.LINE.value: self.parse_point,
            ObjHeader.FACE.value: self.parse_point,
        }
        self.material_parser = {"newmtl": parse_newmtl, "Kd": self.parse_Kd}

        self.material = None
        self.material_table = {}
        self.material_str = ""
        self.obj_str = ""

        self.load_obj(filepath)

    def __str__(self) -> str:
        return ""

    def parse_mttlib(self, params) -> None:
        filename = params[0]
        self.split_and_parse_file(str(Path().absolute()/ "resources" / "obj" / filename), self.material_parser)

    def parse_usemtl(self) -> None:
        pass

    def parse_obj_name(self) -> None:
        pass

    def parse_point(self) -> None:
        pass

    def load_obj(self, filepath: str) -> None:
        # split and parse with default parser
        self.split_and_parse_file(filepath, self.parse_functions)

    def split_and_parse_file(self, filepath: str, parser: Dict) -> None:
        with open(filepath) as f:
            for line in f.readlines():
                l = line.strip().split()
                try:
                    header = split[0] # Header should match the value in our ObjHeader enum
                    params = split[1:]
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
