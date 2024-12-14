# cook your dish here
def catch():
    x,y = map(int,input().split())
    res = 'yes' if y>x else 'no'
    print(res)
t = int(input())
for i in range(t):
    catch()
