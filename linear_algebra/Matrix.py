from .Vector import Vector
class Maxtrix():

    def __init__(self,list):
        self._values = [row[:] for row in list]

    def __add__(self, other):
        assert self.shape() == other.shape(),"The shape of {} and {} is not same".format\
            (self,other)
        return Maxtrix([[a+b for a,b in zip(self.row_vector(i),other.row_vector(i))]
                       for i in range(self.row_num())])

    def __sub__(self, other):
        assert self.shape() == other.shape(), "The shape of {} and {} is not same".format \
            (self, other)
        return Maxtrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                        for i in range(self.row_num())])
    #矩阵数量乘法
    def __mul__(self, k):
        return Maxtrix([[k * e for e in self.row_vector(i)] for i in range(self.row_num())])
    def __rmul__(self, k):
        return Maxtrix([[k * e for e in self.row_vector(i)] for i in range(self.row_num())])

    #矩阵和矩阵相乘
    def dot(self,other):
        if isinstance(other,Vector):
            #矩阵和向量相乘
            assert self.col_num() == len(other),"The matrix col_num is not same as len of vector"
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num())])
        if isinstance(other,Maxtrix):
            # 矩阵和矩阵相乘
            assert self.col_num() == other.row_num(), "The matrix1 col_num is not same as matrix2 row_num"
            return Maxtrix([[self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num())]
                            for i in range(self.row_num())])
    def __truediv__(self, k):
        return (1 / k)*self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    @classmethod
    def zero(cls,shape):
        r,c = shape
        return cls([[0] * c for _ in range(r)])

    def __getitem__(self, pos):
        r,c = pos
        return self._values[r][c]

    def row_vector(self,index):
        return Vector(self._values[index])

    def col_vector(self,index):
        return Vector([row[index] for row in self._values])

    def shape(self):
        return len(self._values),len(self._values[0])

    def row_num(self):
        return len(self._values)

    __len__ = row_num

    def col_num(self):
        return len(self._values[0])

    def size(self):
        r, c = self.shape()
        return r * c

    def __repr__(self):
        return "Matrix = ({})".format(self._values)

    __str__ = __repr__

    #矩阵的转置
    def T(self):
        return Maxtrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])
