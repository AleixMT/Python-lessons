
numbers_keys = ["One", "Two", "Three"]
numbers_values = [1, 2, 3]

numbers_dictionary = {}

for i in range(len(numbers_keys)):
    numbers_dictionary[numbers_keys[i]] = numbers_values[i]

numbers_dictionary["Four"] = 4
print(numbers_dictionary["Three"])
numbers_dictionary.pop("Three")
print(numbers_dictionary)

print(numbers_keys)
print(numbers_dictionary.keys())

print(numbers_dictionary.values())
