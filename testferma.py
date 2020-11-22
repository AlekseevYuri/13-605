def pоw(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    else:
        return pow(x,n//2)*pow(x,n//2)*pow(x,n%2)
        
def test(k):
    if pow(2,k-1)%k == 1 or k ==2:
        print(k,"- простое")
    else:
        print(k," не является простым")
test(1235004)
test(997)
test(991)
test(121)
test(2000029)
test(20001277)
print("А теперь протестируем некоторые числа Кармайкла:")
test(8911)
test(6601)
test(561)
test(1105)

