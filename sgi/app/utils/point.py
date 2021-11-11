from typing import Any
import numpy as np

class Point:
  def __init__(self, x:float, y:float, z:float) -> None:
    self.coord = np.array([x, y, z])


  def getX(self) -> float:
    return self.coord[0]


  def getY(self) -> float:
    return self.coord[1]


  def getZ(self) -> float:
    return self.coord[2]


  def setX(self, x: float) -> None:
    self.coord[0] = x


  def setY(self, y: float) -> None:
    self.coord[1] = y

  def setZ(self, z: float) -> None:
    self.coord[2] = z


  def asnumpy(self) -> None:
    return self.coord


  def transform(self, t:Any) -> None:
    if not isinstance(t, np.ndarray):
        self.coord = np.dot(self.coord,np.array(t))
    else:
        self.coord = np.dot(self.coord,t)
