# cook your dish here
def bill(x,y):
    res = 'YES' if x>=y else 'NO'
    return res  
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(bill(x,y))
