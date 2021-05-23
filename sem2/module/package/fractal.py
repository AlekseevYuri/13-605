import turtle as tl
import math
 
    
def draw(a):
    v = [100*math.sin(a),100*math.cos(a)]
    try:
        for i in range (0,500):
            tl.goto(v[0],v[1])
        
            t=v[0]*math.cos(a)+0.99*v[1]*math.sin(a)
            v[1]=-0.99*v[0]*math.sin(a)+v[1]*math.cos(a)
            v[0] =t
    except:
        print ("Why?")
    
    #tl.done()
    

