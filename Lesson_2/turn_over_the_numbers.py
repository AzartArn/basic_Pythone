number1 = int(input("Введіть число з 5 цифир: "))
number2 = 0

for i in range(5):
    number2 = number2 * 10 + number1 % 10
    number1 = number1 // 10

print(number2)
