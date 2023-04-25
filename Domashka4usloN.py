
N = int(input("Число N: "))

#Якщо N непарне число, виведіть на екран "Weird"
if N % 2 == 1:
    print("weird")

#Якщо N парне число і входить у діапазон від 2 до 5 (включно), виведіть "Not Weird"
elif N% 2 == 0 and N in range(2,6):
    print("Not Weird")

#Якщо N парне число і входить у діапазон від 6 до 20 (включно), виведіть "Weird"
elif N % 2 == 0 and N in range(6,21):
    print("Weird")

#Якщо N непарне число і більше 20, виведіть "Not Weird"
elif N % 2 == 0 and N > 20:
    print("Not Weird")
