from __future__ import division
class Mat:
    def __init__ (self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__ (self,y):
        try:
            z=y%2#Сложно придумать, как ввести эту операцию для матриц.
            pass
        except TypeError: #Если у не является числом, мы действуем с ним как с матрицей.
            return Mat(self.a + y.a,  self.b + y.b,  self.c + y.c,  self.d + y.d)
         
    def __mul__ (self,mat):
        try:
            b=mat%2
            return Mat(self.a * mat,  self.b * mat,  self.c * mat,  self.d * mat)
        except TypeError:
            q = self.a * mat.a + self.b * mat.c
            w = self.a * mat.b + self.b * mat.d
            e = self.c * mat.a + self.d * mat.c
            r = self.c * mat.b + self.d * mat.d
            return  Mat(q,w,e,r)
        
    def T(x):#транспонирование
        x.b += x.c
        x.c = x.b - x.c
        x.b = x.b - x.c
        
    def det(a):#детерминант
        return a.a * a.d - a.c * a.b

    def __sub__(self,q):
        return (self + (-q))
    
    def __rmul__(q,w):    
        return q.__mul__(w)
    
    def __neg__(self):
        return self*-1
    
    def __repr__(x):
        print(x.a,x.b)
        return(str(x.c)+" "+str(x.d)) #Попытка напечатать матрицу таблицей

    #def __str__(x):
        #return(str(x.a)+" "+str(x.b)+" \\" + "\\ "+str(x.c)+" "+str(x.d)) Ecли сделать так, не получится печтать таблицу
        
    def __eq__(self, x):
        try:
            t = x%10
            pass
        except TypeError:
            if self.a == x.a and self.b == x.b and self.c == x.c and self.d == x.d:
                return True
            return False

    def obr (m):#Построение обратной матрицы
        if m.det == 0:
            print ("Неподходящий делитель")
            return ("...")
        else:
            dd = m.det()
            a = m.a
            b = m.b
            c = m.c
            d = m.d
            m_obratnaya = Mat(d/dd, -c/dd, -b/dd, a/dd)
            return(m_obratnaya)
            

    def __truediv__(s,m):#Деление матрицы на что-то
        try:
            return s*(1/m)
        except TypeError:
            try:
                mm = m.obr
                return (s*m.obr())
            except ZeroDivisionError:
                print("Неподходящий делитель")

#Тесты
x = Mat(1,0,0,1)
y = Mat(1,1,1,1)

z=x/1
b = x/y
c = x+y
r = x-y
d = y * 3-3*y*y
print(z)
print(b)
print(c)
print(r)
print(d)

#except ZeroDivisionError:
            #print("Неподходящий делитель")
