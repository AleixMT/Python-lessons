
content_list = []

for i in range(10):
    content_list.append(i * 5)

# Method 1 reverse method of lists
#content_list.reverse()
# Method 2 creating new list from values of first list taken backwards
'''
result_list = []
for i in range(len(content_list) - 1, -1, -1):
    result_list.append(content_list[i])

print(content_list)
print(result_list)
'''
# Method 3 the same but we do not use strange range
'''
result_list = []
for i in range(len(content_list)).__reversed__():
    result_list.append(content_list[i])

print(content_list)
print(result_list)
'''
# Method 4 reverse list manually with just one list (in-place reversion)
'''
print(content_list)
for i in range(int(len(content_list) / 2)):
    tmp = content_list[i]
    content_list[i] = content_list[len(content_list) - 1 - i]
    content_list[len(content_list) - 1 - i] = tmp
print(content_list)
'''
