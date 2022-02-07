
dictionary_destiny = {"One": 1, "Two": 2, "Three": 3}
dictionary_source = {"Four": 4, "Five": 5}

for key_source in dictionary_source.keys():
    dictionary_destiny[key_source] = dictionary_source[key_source]


print(dictionary_destiny)


