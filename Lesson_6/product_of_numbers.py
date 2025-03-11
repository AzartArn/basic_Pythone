input_list = input("Введіть число: ")
number = 11
while number > 9:
    number = 1
    for i in input_list:
        number *= int(i)
    input_list = str(number)
print(input_list)

print("\n🖖 🙊 🫡 🏆 ")
