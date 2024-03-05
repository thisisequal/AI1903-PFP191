import math
def Q_02(a,b,c,x):
    return a*x*x + b*x + c

def Q_03(a,b,c,x):
    tmp = b*b-4*a*c
    if tmp < 0:
        return 0
    else :
        return math.sqrt(tmp)
    
def Q_04(a,b,c):
    if a>b:
        swap(a,b)
    if b>c:
        swap(b,c)
    if a>b:
        swap(a,b)
    if a+b>=c:
        return False
    return True

def Q_05(check,a,b,c):
    if check :
        p = (a+b+c)/2
        S1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return S1
    else:
        print("a, b, c are not side of a triangle")
        return 0
a = int(input())
b = int(input())
c = int(input())
x = int(input())
S1=Q_02(a,b,c,x)
print(S1)
S2=Q_03(a,b,c,x)
print(S2)
a = int(input())
b = int(input())
c = int(input())

check = Q_04(a,b,c)
S1=Q_05(check,a,b,c)