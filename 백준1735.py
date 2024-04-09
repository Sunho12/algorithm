import sys
input = sys.stdin.readline

a,b = map(int,input().split())
c,d = map(int,input().split())

up = a*d + c*b
down = b*d

#최대공약수
def GCD(x,y):
    while y:
        x, y = y, x%y
    return x
gcd = GCD(up, down)

up = int(up/gcd)
down = int(down/gcd)
print(str(int(up))+" "+str(int(down)) )
