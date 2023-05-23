A = {"Артем", "Сергій", "Анастасія", "Вікторія"}
B = {"Ангеліна", "Мирон", "Василіса", "Ірина"}

# Вивести імена людей, які повинні за Червень та Липень
june_and_july_debtors = A.intersection(B)
print("Імена людей, які повинні за Червень та Липень:", june_and_july_debtors)

# Вивести боржників за Липень, у яких немає боргу за Червень
july_debtors_without_june_debt = B.difference(A)
print("Боржники за Липень, у яких немає боргу за Червень:", july_debtors_without_june_debt)


def convert_to_snake_case(string):
    result = ""
    for char in string:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result.lstrip("_")

strings = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_strings = [convert_to_snake_case(string) for string in strings]
print(snake_case_strings)