import random

lists = list()
listend = list()
list_len = random.randint(0,27)

for i in range(list_len):
    lists.append(random.randint(10,99))

if len(lists) <= 1:
    listend.append(lists)
    listend.append(list())
    
else:
    if len(lists) % 2 != 0:
        temp1 = (len(lists) // 2) + 1 
        temp2 = (len(lists) // 2) 
    else:
        temp1= len(lists) // 2
        temp2= len(lists) // 2
    
    listend.append(lists[:temp1])
    listend.append(lists[-temp2:])
    
print(lists)
print(listend)

