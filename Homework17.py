#Завдання 1 Даний файл із довільним текстом, необхідно знайти всі числа у файлі та записати до списку numbers
import re

def find_numbers(filename):
    numbers = []
    with open(filename, 'r') as file:
        text = file.read()
        numbers = re.findall(r'\d+', text)
    return numbers

filename = 'example.txt'  # Замініть на шлях до вашого файлу
numbers = find_numbers(filename)
print(numbers)

#Завдання 2 Запросити у користувача текст та записати його у файл data.txt
text = input("Введіть текст: ")
with open('data.txt', 'w') as file:
    file.write(text)

#Завдання 3 Запросити у користувача число N і запитати N чисел у користувача, потім записати їх у файл numbers.txt через пробіл
N = int(input("Введіть кількість чисел: "))
numbers = []
for i in range(N):
    number = input("Введіть число: ")
    numbers.append(number)

with open('numbers.txt', 'w') as file:
    file.write(' '.join(numbers))

#Завдання 4 Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt, де один рядок = одне число
import random

numbers = [random.randint(1, 1000) for _ in range(100)]
with open('random_numbers.txt', 'w') as file:
    file.write('\n'.join(map(str, numbers)))


#Завдання 5 Даний файл із довільним текстом, потрібно знайти кількість слів у файлі та вивести користувачеві
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = 'example.txt'  # Замініть на шлях до вашого файлу
word_count = count_words(filename)
print("Кількість слів:", word_count)


#Завдання 6 Даний файл, у якому записані числа через пробіл, необхідно вивести користувачу суму цих чисел
def sum_numbers(filename):
    with open(filename, 'r') as file:
        text = file.read()
        numbers = map(int, text.split())
        return sum(numbers)

filename = 'numbers.txt'  # Замініть на шлях до вашого файлу
sum_of_numbers = sum_numbers(filename)
print("Сума чисел:", sum_of_numbers)

#Завдання  Даний файл у якому записаний текст, необхідно вивести топ 5 слів, які найчастіше повторюються, приклад:
from collections import Counter

def top_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read()
        words = re.findall(r'\w+', text)
        counter = Counter(words)
        return counter.most_common(n)

filename = 'example.txt'  # Замініть на шлях до вашого файлу
top_5_words = top_words(filename, 5)
for word, count in top_5_words:
    print(f"'{word}' - {count} разів")

