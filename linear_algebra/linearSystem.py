from linear_algebra.Matrix import Matrix
from linear_algebra.Vector import Vector
from ._global import is_zero

class LinearSystem():

    def __init__(self,A,b):

        assert A.row_num() == len(b), "matrix row num must be equal to length of vector"
        self._m = A.row_num()
        self._n = A.col_num()
        self._b_col = 1
        #增广矩阵
        if isinstance(b,Vector):
            self.Ab = [Vector(A.row_vector(i).return_list() + [b[i]]) for i in range(self._m)]
        elif isinstance(b,Matrix):
            self.Ab = [Vector(A.row_vector(i).return_list() + b.row_vector(i).return_list()) for i in range(self._m)]
            self._b_col = b.col_num()
        #主元所在的列
        self.pivots = []

    def _max_row(self,index_i,index_j):

        max_cur,row_max= self.Ab[index_i][index_j],index_i
        for i in range(index_i+1,self._m):
            if self.Ab[i][index_j] > max_cur:
                max_cur,row_max = self.Ab[i][index_j],i
        return row_max

    def _forward(self):
        #定义循环
        i,j = 0,0
        while i < self._m and j < self._n:
            #找到i行之后第j列的最大值所在行
            max_row = self._max_row(i,j)
            #交换
            self.Ab[i],self.Ab[max_row] = self.Ab[max_row],self.Ab[i]
            if is_zero(self.Ab[i][j]):
                j += 1
            else:
                #归一
                self.Ab[i] = self.Ab[i] / self.Ab[i][j]
                #消元
                for k in range(i+1,self._m):
                    self.Ab[k] = self.Ab[k] - self.Ab[i] * self.Ab[k][j]
                self.pivots.append(j)
                i += 1

    def _backward(self):

        for i in range(len(self.pivots)-1,-1,-1):
            j = self.pivots[i]
            for k in range(i-1,-1,-1):
                self.Ab[k] = self.Ab[k] - self.Ab[i] * self.Ab[k][j]

    def goss_jordan_elimination(self):

        self._forward()
        self._backward()
        self.fancy_print()
        for i in range(len(self.pivots),self._m):
            for j in range(self._b_col):
                col = -1 - j
                if not is_zero(self.Ab[i][col]):
                    return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join([str(self.Ab[i][j]) for j in range(self._n)]),end=" ")
            print("|" + str(self.Ab[i][-1]))


def inv(A):

    if A.col_num() != A.row_num():
        return None

    ls = LinearSystem(A,Matrix.identity(A.row_num()))
    if not ls.goss_jordan_elimination():
        return None

    invA = [ls.Ab[i][A.row_num():] for i in range(A.row_num())]
    return Matrix(invA)

def lu(matrix):

    assert matrix.row_num() == matrix.col_num(), "matrix must be a square matrix"

    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        print(A[i][i])
        #check A[i][i]能否成为主元
        if is_zero(A[i][i]):
            return None,None
        else:
            for j in range(i+1,n):
                p = A[j][i] / A[i][i]
                A[j] = A[j] - p * A[i]
                L[j][i] = p

    return Matrix(L),Matrix(A)