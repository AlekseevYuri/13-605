class Mat:
    def __init__ (self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def p (self,y):
        return Mat(self.a + y.a,  self.b + y.b,  self.c + y.c,  self.d + y.d)
           
    def m (self,y):
        return Mat(self.a - y.a,  self.b - y.b,  self.c - y.c,  self.d - y.d)
            
    def mult (self,const):
        return Mat(self.a * const,  self.b * const,  self.c * const,  self.d * const)
    
    def Mult (self, mat):
        q = self.a * mat.a + self.b * mat.c
        w = self.a * mat.b + self.b * mat.d
        e = self.c * mat.a + self.d * mat.c
        r = self.c * mat.b + self.d * mat.d
        return  Mat(q,w,e,r)
        
    def pr(x):
        print(x.a,x.b)
        print(x.c,x.d)
        
    def T(x):
        x.b += x.c
        x.c = x.b - x.c
        x.b = x.b - x.c
    def det(a):
        return a.a * a.d - a.c * a.b
        
x = Mat(1,0,0,1)
y = Mat(7,7,3,7)
z =x.p(y)
z.T()
z=z.mult(10)
z.pr()
z=z.Mult(x)
z.pr()
z=z.Mult(z)
z.pr()
z.T()
z.pr()
z.T()
z.pr()
print(z.det())
print((z.Mult(z)).det())
