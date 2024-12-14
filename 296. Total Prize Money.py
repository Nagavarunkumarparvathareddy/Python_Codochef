# cook your dish here
def amounnt(x,y):
   return 10*x+(90*y)
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(amounnt(x,y))
