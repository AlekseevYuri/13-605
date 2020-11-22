import math
def test(x):
    
    if x%2  == 0 and x>2 or x ==1:
        print(x," не является простым")
        return
    if x<4:
        print (x,"- простое число")
    else:
        k=math.sqrt(x)//1
        if k%2 ==0:
            k=k+1
        t(x,k)
        
def t(x,k):
    if x%k ==0:
        print(x," не является простым")
        return
    if k == 3:
        print (x,"- простое число")
        return
    t(x,k-2)
test(101)
test(2)
test(2000029)
print("а это уже слишком...(проверка числа 20001277, оно простое) ")
test(20001277)
