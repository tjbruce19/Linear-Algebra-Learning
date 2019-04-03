from linear_algebra.Matrix import Matrix
from linear_algebra.Vector import Vector
from ._global import is_zero

class LinearSystem():

    def __init__(self,A,b):

        assert A.row_num() == len(b), "matrix row num must be equal to length of vector"
        self._m = A.row_num()
        self._n = A.col_num()
        #增广矩阵
        self.Ab = [Vector(A.row_vector(i).return_list() + [b[i]]) for i in range(self._m)]
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
                    self.Ab[k] = self.Ab[k] - self.Ab[i] * self.Ab[k][i]
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

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join([str(self.Ab[i][j]) for j in range(self._n)]),end=" ")
            print("|" + str(self.Ab[i][-1]))