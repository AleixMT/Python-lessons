# Initialize a list with random integers
# Compute mean and the standard deviation

import random
LIST_SIZE = 100

random_list = []

for _ in range(LIST_SIZE):
    random_list.append(int(random.random() * 1000))

print(random_list)

# Way of computing mean 1
print(sum(random_list) / len(random_list))

# Way of computing mean 2
random_list_sum = 0
for i in range(LIST_SIZE):
  random_list_sum = random_list_sum + random_list[i]

print(random_list_sum / len(random_list))




