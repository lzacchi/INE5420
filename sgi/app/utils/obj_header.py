from enum import Enum

class ObjHeader(Enum):
    MTLLIB = "mtllib"
    USEMTL = "usemtl"
    OBJ_NAME = "o"
    VERTICE = "v"
    POINT = "p"
    LINE = "l"
    FACE = "f"
    NEWMTL = "newmtl"
    KD = "Kd"
    # W = auto() ?

    def __str__(self) -> str:
        return super().__str__()
