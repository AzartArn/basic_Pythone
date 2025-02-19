import random

list_number = list()

for i in range(20):
    list_number.append(random.randint(0,20))
    
print(list_number)
    
for i in range(20):
    if list_number[i] == 0:
        tmp = list_number.pop(i)
        list_number.append(tmp)
        
print(list_number)