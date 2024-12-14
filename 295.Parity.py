# cook your dish here
def chocolate(x):
    res = 'yes' if x%2 == 0 else 'no'
    return res 
t = int(input())
for i in range(t):
    x = int(input())
    print(chocolate(x))
