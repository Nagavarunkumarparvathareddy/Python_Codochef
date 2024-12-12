# cook your dish here
def rank(x):
    if x <= 10:
        return 'YES'
    else:
        return 'NO'
t = int(input())
for i in range(t):
    x = int(input())
    print(rank(x))
