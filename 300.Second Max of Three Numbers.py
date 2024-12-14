# cook your dish here
def secondmax():
    x,y,z = map(int,input().split())
    if x>y and z>x:
        print(x)
    if y>x and y<z:
        print(y)
    if z>x and z<y:
        print(z)
    if x<y and x>z:
        print(x)
    if y<x and y>z:
        print(y)
    if z<x and z>y:
        print(z)
t = int(input())
for i in range(t):
    secondmax()
