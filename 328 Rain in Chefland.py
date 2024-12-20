# cook your dish here
t = int(input())
for i in range(t):
    r = int(input())
    if r<3:
        print('light')
    elif r>=3 and r<7:
        print('moderate')
    else:
        print('heavy')
