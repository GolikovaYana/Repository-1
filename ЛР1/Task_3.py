list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

number_players = int(len(list_players) / 2)
team_1 = list_players[:number_players]
team_2 = list_players[number_players:]
print(team_1)
print(team_2)
