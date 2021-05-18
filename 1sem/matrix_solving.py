import itertools
from numbers import Number
class MatrixArithmeticError(IndexError):
    pass

def sum (l):#Вспомогательная функция, суммирующая элементы списка
    s = 0
    for i in range (len(l)):
        s += l[i]
    return s

def ssum (self, other,k): #Прибавление к первой строке второй строки, умноженной на к
    if len(self)==len(other):
        for i in range (len(self)):
            self[i]+=other[i]*k
        return(self)
    else:
        raise MatrixArithmeticError("Складываются строки/столбцы разной длины")
    
def GAUSS(m):
    if m.H+1==m.L:
        gauss_down(m)
        gauss_up(m)
        norm(m)
    
def norm (m):#Улучшает матрицу ответов
    for i in range(m.H):
        if m.mat[i][i]!=0:
            m.mat[i][m.H] *=1/m.mat[i][i]
            m.mat[i][i]=1



            
def gauss_down(m):#Прямой ход метода Гаусса
    for i in range (m.H):
        m.sort(i,i)
        if m.mat[i][i] !=0:
            for ii in range (i+1,m.H):
                if m.mat[i][i]!=0:
                    m.transv(i,ii,-m.mat[ii][i]/m.mat[i][i])
                

def gauss_up(m):#Обратный ход метода Гаусса
    for i in range (0,m.H):
        if m.mat[m.H-1-i][m.H-1-i] !=0:
            for ii in range (0,i):
                if m.mat[i][i]!=0:
                    m.transv(i,ii,-m.mat[ii][i]/m.mat[i][i])




       
class matrix:#Для удобства.

    def __init__(self, m):
        self.mat = m.copy()
        self.L = len(m[0])
        self.H = len(m)

    def __mul__ (self, other):#Умножение матриц.
        if isinstance(other, Number):
            return matrix([  [  self.mat[i][j]*other  for j in range (self.L)] for i in range (self.H)])
        else:
            if self.L == other.H:
                return matrix([  [  sum([self.mat[i][k]*other.mat[k][j] for k in range(self.L)])  for j in range (other.L)] for i in range (self.H)])
            else:
                raise MatrixArithmeticError("Результат умножения не определен")
        
    def __rmul__ (self,other):#Второе умножение. Вызовется, если матрица умножается на число. Умножение на число коммутативно.
        return self.__mul__(other)
  
    
    def trans (self, i, j): #Переставить строки с номерами i, j.
        a = self.mat[i]
        self.mat[i] = self.mat[j]
        self.mat[j] = a

    def transv (self, i, j, multiplier):#Прибавление строки i, умноженной на multiplier, к строке j.
        self.mat[j] = ssum(self.mat[j], self.mat[i], multiplier)

    def sort (self,j,start):#Упорядочивает строки по j-му индексу (ненулевые впереди нулевых).
        for i in range (self.H+1):
            for ii in range (self.H-1):
                if self.mat[ii][j]==0 and self.mat[ii+1][j] !=0 and ii>start-1:
                    self.trans(ii,ii+1)
    def p (self):#Красивый вывод.
        for i in range (self.H):
            print(self.mat[i])
        
#Пример использования.
mm = matrix([[3.0, 2.0, 4.0, 1.0,11111],
    [1.5, 2.0, 1.5, 2.0,0],
    [1.0, 6.0, 0.0, 4 ,1111 ],
    [2.0, 1.0, 4.0, 3  ,1]
])
GAUSS(mm)


mm.p()
