from linear_algebra.Vector import Vector
from linear_algebra.Matrix import Matrix
from linear_algebra.linearSystem import LinearSystem,inv

if __name__ == "__main__":
    # A = Matrix([[1,2,4],[3,7,2],[2,3,3]])
    # b = Vector([7,-11,1])
    # ls = LinearSystem(A,b)
    # ls.goss_jordan_elimination()

    A1 = Matrix([[1, -1, 2, 0, 3], [-1,1,0,2,-5],[1,-1,4,2,4], [-2,2,-5,-1,-3]])
    b1 = Vector([1,5,13,-1])
    ls1 = LinearSystem(A1, b1)
    ls1.goss_jordan_elimination()

    A = Matrix([[1,2],[3,4]])
    invA = inv(A)
    print(invA)
    print(invA.dot(A))
