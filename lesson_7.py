# Завдання 1:Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
word = input("Введіть слово: ")

if word == word[::-1]:
    print("+")
else:
    print("-")

# 2 Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'

text = input("Введіть текст: ")
word = input("Введіть слово: ")

if word in text:
    print("YES")
else:
    print("NO")

# 3 Користувач вводить рядок. Якщо вона починається на 'abc', замінити їх на 'www', інакше додати в кінець рядка 'qqq'.

string = input("Введіть рядок: ")

if string.startswith("abc"):
    new_string = string.replace("abc", "www", 1)
    print(new_string)
else:
    new_string = string + "qqq"
    print(new_string)

# 4 Користувач вводить текст, видалити всі цифри в тексті і вивести рядок користувачеві.

text = input("Введіть текст: ")
new_text = ""
for char in text:
    if not char.isdigit():
        new_text += char
print(new_text)

# 5 Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"

email = input("Введіть адресу електронної пошти: ")
if '@' in email and '.' in email:
    print("YES")
else:
    print("NO")