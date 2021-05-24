import math
def test(x):
    
    if x%2  == 0 and x>2 or x ==1:
        #print(x," не является простым")
        return False
    if x<4:
        #print (x,"- простое число")
        return True
    else:
        k=math.sqrt(x)//1
        if k%2 ==0:
            k=k+1
        t(x,k)
        return True
        
def t(x,k):
    if x%k ==0:
        #print(x," не является простым")
        return False
    if k == 3:
        #print (x,"- __простое число")
        return True
    t(x,k-2)


