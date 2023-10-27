users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict = {"Общее количество": 0, "Уникальные посещения": 0}
count = len(users)
unic = len(set(users))
dict["Общее количество"] = int(count)
dict["Уникальные посещения"] = int(unic)
print(dict)
