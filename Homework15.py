import json

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = {}

# Об'єднання словників A і B
for key, value in A.items():
    if key in B:
        # Колізія ключів - створюємо список значень
        C[key] = [value, B[key]]
    else:
        C[key] = value

# Додавання до C ключів, яких немає в A
for key, value in B.items():
    if key not in A:
        C[key] = value

# Запис результату у файл у форматі JSON
with open('result.json', 'w') as file:
    json.dump(C, file)
