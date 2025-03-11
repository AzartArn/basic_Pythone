import string

str_range = input("Введіть діапазон букв: ")

index1 = string.ascii_letters.find(str_range[0])
index2 = string.ascii_letters.find(str_range[-1])

if index1 > index2:
    print(string.ascii_letters[index1:], string.ascii_letters[:index2+1], sep='')
else:
    print(string.ascii_letters[index1:index2+1])

print("\n🖖 🙊 🫡 🏆")
