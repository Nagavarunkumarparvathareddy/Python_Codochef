import math
n = int(input())
s = str(n)
lst = list(s)
num_sum = 0
for ele in lst:
    num_sum += math.factorial(int(ele))
if n == num_sum:
    print('Strong Number')
else:
    print('Not a strong Number')
