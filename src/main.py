'''
elems = ["thing", "thing2", "thing", "ice"]

for i in range(len(elems)):
    print(elems[i])

for i in elems:
    print(i)

dictio = {}
dictio["onestring"] = "other"
dictio["pot"] = "potat"
dictio["sfsf"] = "sdf"


for i in dictio.keys():
    print(dictio[i])

print()

for i in dictio.values():
    print(i)

# result1 is integer sum
result1 = 2 + 3
print(result1)
# result is string concatenation
result2 = "2" + "3"
print(result2)
# Casting integer to float (real number)
print(float(result1))


# lists and dictionaries, can be modified in  function
def fill_list(the_list):
    if len(the_list) == 0:
        the_list.append(0)
    elif len(the_list) == 1:
        the_list.pop(0)
    else:
        the_list.append(4)


new_list = []
fill_list(new_list)

print(new_list)

'''

def change_number(number):
    if number != 0:
        number = 0
    return number

number = 2

result = change_number(number)


print(result)

range(0, 100, 1)  # = range(100)






