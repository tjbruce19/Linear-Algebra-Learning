from linear_algebra.Matrix import Matrix
from linear_algebra.Vector import Vector

class LinearSystem():

    def __init__(self,A,b):

        assert A.row_num() == len(b), "matrix row num must be equal to length of vector"
        self._m = A.row_num()
        self._n = A.col_num()
        #判断矩阵为方阵
        # TODO:is not must
        assert A.row_num() == A.col_num(), "matrix row num must be equal to matrix col num"

        self.Ab = [Vector(A.row_vector(i).return_list() + [b[i]]) for i in range(self._m)]

    def _max_row(self,index):

        max_cur,row_max= self.Ab[index][index],index
        for i in range(index+1,self._m):
            if self.Ab[i][index] > max_cur:
                max_cur,row_max = self.Ab[i][index],i
        return row_max

    def _forward(self):
        for i in range(self._n):
            #找到i行之后第i列的最大值所在行
            max_row = self._max_row(i)
            #交换
            self.Ab[i],self.Ab[max_row] = self.Ab[max_row],self.Ab[i]
            #归一
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]
            #消元
            for j in range(i+1,self._m):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]


    def _backward(self):
        for i in range(self._m-1,-1,-1):
            #归一
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]
            for j in range(i-1,-1,-1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def goss_jordan_elimination(self):

        self._forward()
        self._backward()
        self.fancy_print()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join([str(self.Ab[i][j]) for j in range(self._n)]),end=" ")
            print("|" + str(self.Ab[i][-1]))