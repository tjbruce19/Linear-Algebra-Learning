import math
from ._global import ACCURACY
class Vector():

    def __init__(self,lst):
        self._values = lst

    def __iter__(self):
        return self._values.__iter__()
    #向量的模
    def norm(self):
        return math.sqrt(sum(e**2 for e in self))
    #向量的方向
    def normalize(self):
        return Vector(self._values) / self.norm()

    #零向量
    @classmethod
    def zero(cls, dim):
        return Vector([0] * dim)

    # 向量的数量乘法
    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return Vector([k * e for e in self])
    #数量除法
    def __truediv__(self, k):
        if k < ACCURACY:
            raise ZeroDivisionError("k CANT BE Zero")
        return Vector([1/k * e for e in self])
    # 向量取正/负
    def __pos__(self):
        return Vector([1 * e for e in self])

    def __neg__(self):
        return Vector([-1 * e for e in self])

    #向量的减法
    def __sub__(self, other):
        assert len(self) == len(other), "ERROR:Length vector must be same."
        return (Vector([a - b for a, b in zip(self, other)]))
    #向量的加法
    def __add__(self, other):
        assert len(self) == len(other),"ERROR:Length vector must be same."
        return (Vector([a+b for a,b in zip(self,other)]))

    #向量的维度
    def __len__(self):
        return len(self._values)

    #向量中的数
    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "Vector(%s)" % self._values

    def __str__(self):
        return "(%s)" % ", ".join(str(e) for e in self._values)
