number = int(input("Введіть число з 4 цифир: "))

m = 10000
k = 1000

for i in range(4):
    print(number%m//k)
    m = m // 10
    k = k //10
