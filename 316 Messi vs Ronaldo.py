# cook your dish here
mg,ma,rg,ra = map(int,input().split())
if (mg*2)+ma == (rg*2)+ra:
    print('Equal')
elif (mg*2)+ma > (rg*2)+ra:
    print('Messi')
else :
    print('Ronaldo')
