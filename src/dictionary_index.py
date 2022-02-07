
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": [70, 80]
        }
    }
}



print(sampleDict["class"]["student"]["marks"][0])

# This is the same...
sampleDict_inner = sampleDict["class"]
sampleDict_inner_inner = sampleDict_inner["student"]
# ... as this
sampleDict_inner_inner_b = sampleDict["class"]["student"]

tuple_one = (1, 2)
