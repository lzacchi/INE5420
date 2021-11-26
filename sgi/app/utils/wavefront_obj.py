"""Wavefront.obj File handler"""

import traceback
from pathlib import Path
from enum import Enum, auto
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from typing import List, Dict, Union
from utils.wireframe_structure import WireframeStructure
from utils.obj_header import ObjHeader


WHITE = QColor(255, 255, 255)




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
        return f"Obj reader has read: {self.vertices}"

    def parse_mttlib(self, params:list) -> None:
        path = str(Path().absolute()/ "resources" / "obj" / params[0])
        self.split_and_parse_file(path, self.material_parser)

    def parse_usemtl(self, params:list) -> None:
        material_file = params[0]
        self.material = self.material_table[material_file]

    def parse_obj_name(self, params:list) -> None:
        self.obj_str = params[0]

    def parse_vertice(self, params: list) -> None:
        x, y, _ = params
        print(f"Parsed vertice {x} {y} {_}")
        self.vertices.append((float(x), float(y)))

    def parse_elements(self, params:list) -> None:
        points = []
        for v in params:
            index = int(v) if v[0] == "-" else int(v) - 1
            points.append(self.vertices[index])
        
        no_color = not self.material
        if no_color:
            self.material = WHITE
        wireframe = WireframeStructure(
            points, self.index, self.material, self.normalization_value, self.transformations
        )
        wireframe.set_name(self.obj_str)
        self.wireframes.append(wireframe)
        
        # Clear variables and increment index
        self.material = WHITE
        self.obj_str = ""
        self.index += 1

    def parse_newmtl(self, params: list) -> None:
        self.material_str = params[0]

    def parse_Kd(self, params: list) -> None:
        color = QColor(
            int(float(params[0]) * 255),
            int(float(params[1]) * 255),
            int(float(params[2]) * 255),
        )
        self.material_table[self.material_str] = color
        self.material_str = ""

    def load_obj(self, filepath: str) -> None:
        # split and parse with default parser
        self.split_and_parse_file(filepath, self.parse_functions)

    def split_and_parse_file(self, filepath: str, parser: Dict) -> None:
        with open(filepath) as f:
            lines = f.readlines()
            for rawline in lines:
                line = rawline.strip().split()
                try:
                    if len(line) >= 2:
                        header = line[0] # Header should match the value in our ObjHeader enum
                        params = line[1:]
                        parser[header](params)
                    else:
                        continue # Skipping blank or invalid line
                except Exception as e:
                    error_index = lines.index(rawline)+1
                    print(f"Error '{e}' parsing line {error_index} with content {rawline}")
                    print("===")
                    traceback.print_exc()
                    print("===")
                    continue


class ObjWriter:
    def __init__(self, wireframes: list, scene_name: str, denormalization_matrix: list) -> None:
        self.scene_name = scene_name
        self.wireframes = wireframes
        self.denormalization_matrix = denormalization_matrix

    def __str__(self) -> str:
        return f"Saving scene: {self.scene_name}"

    def write_obj(self) -> None:
        material_line = f"{ObjHeader.MTLLIB.value} {self.scene_name}.mtl\n"
        obj_file = [material_line]
        material_file: List[str] = []

        for w in self.wireframes:
            obj_info, material_info = w.to_obj_str(self.denormalization_matrix)
            obj_file.extend(obj_info)
            material_file.extend(material_info)

        filepath = str(Path().absolute() / "resources" / "obj" / self.scene_name)
        self.save_file(filepath + ".obj", obj_file)
        self.save_file(filepath + ".mtl", material_file)


    def save_file(self, filename: str, lines: List[str]) -> None:
        with open(filename, "w") as writer:
            for l in lines:
                writer.write(l)
