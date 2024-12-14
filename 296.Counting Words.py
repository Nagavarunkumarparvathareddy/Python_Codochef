# cook your dish here
def words():
    x,y = map(int,input().split())
    return x*y
t = int(input())
for i in range(t):
    print(words())
