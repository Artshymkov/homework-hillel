n = int(input())  # кількість файлів
files = {}  # словник для зберігання файлів та їх допустимих операцій

# Заповнення словника файлів та їх операцій
for x in range(n):
    filename, permissions = input().split(maxsplit=1)
    files[filename] = set(permissions)

m = int(input())  # кількість запитів

# Обробка запитів
for x in range(m):
    operation, filename = input().split()

    if filename in files and operation in files[filename]:
        print("OK")
    else:
        print("Access denied")
