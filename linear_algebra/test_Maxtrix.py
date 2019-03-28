from linear_algebra.Matrix import Maxtrix
from linear_algebra.Vector import Vector

if __name__=="__main__":
    matrix = Maxtrix([[1,2,2],[3,4,4]])
    print(matrix)
    print(matrix[0,1])
    print(matrix.shape())
    print(matrix.size())
    print(matrix.row_vector(1))
    print("col_vector：{}".format(type(matrix.col_vector(1))))
    print(len(matrix))

    print(Maxtrix.zero((2,3)))
    vec = Vector([1,2,3])
    matr1 = Maxtrix([[1,2,2],[3,4,4],[2,3,2]])
    print(matrix.dot(vec))
    print(matrix.dot(matr1))