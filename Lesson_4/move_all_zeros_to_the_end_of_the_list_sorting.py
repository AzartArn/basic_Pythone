import random

list_number = list()

for i in range(10):
    list_number.append(random.randint(0,9))
    
print(list_number)

list_number.sort(key=lambda x: x == 0)

print(list_number)