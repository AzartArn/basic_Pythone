import random

str1 = "Оберіть довжину списку довжина має бути додатньою і не більше 20 : "
lists = list()

list_len = int(input(str1))

list_len = list_len if list_len <= 20 else 20

for i in range(list_len):
    lists.append(random.randint(10,99))
    
print(lists)
    
if len(lists) > 1:
    lists.insert(0, lists.pop())
    print(lists)