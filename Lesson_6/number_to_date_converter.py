
number = int(input("Введіть число: "))

if number < 0:
    number = 0
elif number > 8640000:
    number = 8640000

seconds = number % 60
minutes = number // 60 % 60
hours = number //60 // 60 % 24
days = number //60 // 60 // 24

print_str = ''

if days < 1:
    print_str = f"{hours:02}:{minutes:02}:{seconds:02}"
elif days == 1:
    print_str = f"{days} day, {hours:02}:{minutes:02}:{seconds:02}"
else:
    print_str = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"


print(print_str)

print("\n🖖 🙊 🫡 🏆")
