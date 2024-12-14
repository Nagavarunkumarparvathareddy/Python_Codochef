# cook your dish here
def party():
    x,y = map(int,input().split())
    if y>=x:
        print('yes')
    else:
        print('no')
t = int(input())
for i in range(t):
    party()
