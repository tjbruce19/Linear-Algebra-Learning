from linear_algebra.Vector import Vector
from linear_algebra.Matrix import Matrix
from linear_algebra.linearSystem import LinearSystem

if __name__ == "__main__":
    A = Matrix([[1,2,4],[3,7,2],[2,3,3]])
    b = Vector([7,-11,1])
    ls = LinearSystem(A,b)
    ls.goss_jordan_elimination()