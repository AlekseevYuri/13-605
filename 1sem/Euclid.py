def ab(a):
    if a<0:
        return-a
    else:
        return a


    
def gcd (a,b):
    a = ab(a)
    b = ab(b)
    if a*b ==0:
        return a+b
    else:
        if a>b:
           return gcd(a%b,b)
        else:
           return gcd(a,b%a)
print("gcd(-123,1458765)=",gcd(-123,1458765))
print("gcd(12,144)=",gcd(12,144))
print("gcd(12146345,997)=",gcd(12146345,997))
print("gcd(0,0)=",gcd(0,0))
print("gcd(1000000,-1000)=",gcd(1000000,-1000))

