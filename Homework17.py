def cache_decorator(func):
    cache = {}  # словник для зберігання вхідних та вихідних даних функції

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  # створення унікального ключа з вхідних аргументів

        if key in cache:
            print('Результат взятий з кешу')
            return cache[key]  # повертаємо результат з кешу, якщо він вже збережений

        result = func(*args, **kwargs)  # викликаємо оригінальну функцію
        cache[key] = result  # зберігаємо результат в кеші

        return result

    return wrapper


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)


print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
