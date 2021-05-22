import turtle as tl
import math


def c(x):
    
    return (x+3)%5-4
    
def draw(a):
    v = [a,a]
    
    for i in range (0,5):
        tl.goto(v[0],v[1])
        
        a += c(a)
        

        t=v[0]*c(a)+v[1]*c(c(a))
        v[1]=v[0]*c(c(c(a)))+v[1]*c(c(c(c(a))))
        v[0] =t
    #tl.done()
    

