# cook your dish here
def battery():
    x = int(input())
    res = 'yes' if x >= 80 else 'no'
    return res
t = int(input())
for i in range(t):
    print(battery())
