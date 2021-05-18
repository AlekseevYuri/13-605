def repeat(q):
    
#СОДЕРЖАТЕЛЬНАЯ ЧАСТЬ:
    def d(g): 
        def f(r):
            for i in range (0,q):
                r = g(r)
            return r
        return f
    return d
#содержательная часть.


@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2


#МОИ ТЕСТЫ:

@repeat(5)
def mult(x):
    return x**2



print(mul_2(10))
print(mul_2(7))
print(mult(100))
print(plus_1(99))

print (repeat)###
print(mul_2)###

#мои тесты.

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
