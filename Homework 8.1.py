groups = {"Ivan": "молодь",
    "Kira": "молодь",
    "Marya": "дорослі",
    "Alexander": "дорослі",
    "Anastasya": "Люди похилого віку"
}

user_name = input("Введіть ім'я користувача: ")

if user_name in groups:
    print(f"Вікова група {user_name}: {groups[user_name]}")
else:
    print(f"Ім'я {user_name} не знайдено в базі.")