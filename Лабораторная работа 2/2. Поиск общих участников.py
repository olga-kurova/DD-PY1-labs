# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=',') -> list:
    group1_set = set(name.strip() for name in group1.split(delimiter))
    group2_set = set(name.strip() for name in group2.split(delimiter))

    common_participants = group1_set.intersection(group2_set)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter=',')
print(common_participants)