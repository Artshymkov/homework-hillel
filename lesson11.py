# завдання 1:Запросити користувача 5 чисел і записати їх до списку

numbers = []
for i in range(5):
    num = int(input("Введіть число: "))
    numbers.append(num)

print("Список чисел:", numbers)


# Завдання 2:Даний список A = [1, 2, 3, 4, 5] Видалити останнє число зі списку

A = [1, 2, 3, 4, 5]
A.pop()

print("Список A після видалення останнього числа:", A)




# Завдання 3:Запросити користувача 10 чисел і записати їх до списку A .Запросити у користувача число N.Вивести користувачу скільки у списку A повторюється число N

A = []
for i in range(10):
    num = int(input("Введіть число: "))
    A.append(num)

N = int(input("Введіть число N: "))
count = A.count(N)

print("Кількість повторень числа N у списку A:", count)



#Завдання 4:Запросити у користувача число N.Запросити користувача N чисел і записати їх до списку A.Вивести список у зворотній послідовності

N = int(input("Введіть число N: "))
A = []
for i in range(N):
    num = int(input("Введіть число: "))
    A.append(num)

A.reverse()

print("Список A у зворотній послідовності:", A)


# Завдання 5:Запросити користувача 5 чисел і записати їх до списку A.Записати всі числа зі списку A які більше 5 до списку C

A = []
for i in range(5):
    num = int(input("Введіть число: "))
    A.append(num)

C = [num for num in A if num > 5]

print("Список чисел більше 5:", C)



# Завдання 6:Запросити у користувача число N.Запросити користувача N цілих чисел і записати їх до списку A.Знайти в ньому мінімальну та максимальну кількість за допомогою циклу (заборонено використовувати функцію min, max, sorted, sort). Вивести ці числа.

N = int(input("Введіть число N: "))
A = []
for i in range(N):
    num = int(input("Введіть число: "))
    A.append(num)

min_num = A[0]
max_num = A[0]

for num in A:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Мінімальне число:", min_num)
print("Максимальне число:", max_num)


# Завдання 7: Користувач вводить текст потрібно вивести кількість цифр у цьому тексті

text = input("Введіть текст: ")
digits_count = sum(char.isdigit() for char in text)

print("Кількість цифр у тексті:", digits_count)

