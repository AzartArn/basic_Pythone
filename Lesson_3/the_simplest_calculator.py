#  модифікація калькулятора для завдання 5.2
import os

while True:
    listsdictf = ['\nВведіть перше число: ', '\nВедіть операцію: ', '\nВведіть друге число: ']
    listoperf = [' ', ' ', ' ']
    
    for i in range(len(listsdictf)):
        listoperf[i] = input(listsdictf[i])
    
    if listoperf[1] == "+":
        rez = int(listoperf[0]) + int(listoperf[2])
        print(f"{listoperf[0]} {listoperf[1]} {listoperf[2]} = {rez}")
    elif listoperf[1] == "-":
        rez = int(listoperf[0]) - int(listoperf[2])
        print(f"{listoperf[0]} {listoperf[1]} {listoperf[2]} = {rez}")
    elif listoperf[1] == "*":
        rez = int(listoperf[0]) * int(listoperf[2])
        print(f"{listoperf[0]} {listoperf[1]} {listoperf[2]} = {rez}")
    elif listoperf[1] == "/" and int(listoperf[2]) != 0:
        rez = int(listoperf[0]) / int(listoperf[2])
        print(f"{listoperf[0]} {listoperf[1]} {listoperf[2]} = {rez}")
    else:
        print("""Не вірно обрана операція!!\n
                Лише допустимі такі дії: +, -, *, / \n
                або ви вирішили поділити на 0""")
    
    question = input("Якщо хочете продовдити роботу введіть 'так' або 'т': ")
    if question == 'так' or question == 'т':
        os.system('clear')
    else:
        break