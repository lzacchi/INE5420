import numpy as np

class Point:
  def __init__(self, x:int, y:int, z:int) -> None:
    self.coord = np.array([x, y, z])

  def getX(self) -> int:
    return self.coord[0]

  def getY(self) -> int:
    return self.coord[1]

  def getZ(self) -> int:
    return self.coord[2]

  def setX(self, x: int) -> None:
    self.coord[0] = x

  def setY(self, y: int) -> None:
    self.coord[1] = y

  def setZ(self, z: int) -> None:
    self.coord[2] = z


  def asnumpy(self):
    return self.coord

  def transform(self, t) -> None:
    if not isinstance(t, np.ndarray):
        self.coord = np.dot(self.coord,np.array(t))
    else:
        self.coord = np.dot(self.coord,t)
