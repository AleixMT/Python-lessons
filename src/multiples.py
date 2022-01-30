'''
From all the numbers to 0 to 100 select the numbers that are multiple of 3,
the numbers that are multiple of 7. numbers multiple of 3 and 7
'''

multiple_3 = []
multiple_7 = []
multiple_3_7 = []
for i in range(1, 100):
    # Multiple of 3
    if i % 3 == 0:
        multiple_3.append(i)
    if i % 7 == 0:
        multiple_7.append(i)

for i in range(len(multiple_3)):
    if multiple_3[i] in multiple_7:
        multiple_3_7.append(multiple_3[i])

print(multiple_3_7)
