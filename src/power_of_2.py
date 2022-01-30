'''
Get the numbers from 0 to N that are power of two.


# Method 1 using iterative division
def isPowerOf2(n):
    while n > 1:
        if isDivisibleBy2(n) == 1:
            n = int(n / 2)
        else:
            return 0
    return 1


def isDivisibleBy2(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


power_of2 = []
for i in range(100):
    if isPowerOf2(i) == 1:
        power_of2.append(i)

print(power_of2)

'''

import math

N = 1000
power_of2 = []

def Log2(n):
    return math.log10(n) / math.log10(2)

for i in range(1, N):
    if int(Log2(i)) == Log2(i):
        power_of2.append(i)
    else:
        pass

print(power_of2)