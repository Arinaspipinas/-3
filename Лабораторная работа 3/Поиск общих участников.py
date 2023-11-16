# TODO Напишите функцию find_common_participants

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(a, b, delimiter=","):
    list_first = a.split(delimiter)
    list_second = b.split(delimiter)
    intersection_list = sorted(set(list_first).intersection(list_second))
    return intersection_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

delimiter = "|"

result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(result)

