# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, delimiter= ','):
    set_1 = set(group_1.split(delimiter))
    set_2 = set(group_2.split(delimiter))

    common_participants = list(set_1.intersection(set_2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group,
                                               participants_second_group, '|')

# TODO Провеьте работу функции с разделителем отличным от запятой
print(common_participants)