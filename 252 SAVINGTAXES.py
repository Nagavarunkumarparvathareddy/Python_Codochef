# cook your dish here
def tax(x,y):
    return x-y
t = int(input())
for i in range(t):
    x,y = list(map(int,input().split()))
    print(tax(x,y))
