def remove_from_list(list, val):
    return [value for value in list if value != val]


data_list = list(map(float, input().split(' ')))

data_list.sort()
new_list = data_list
final_list = []
while data_list:
    final_list.append(int(data_list[0]))
    data_list = remove_from_list(data_list, data_list[0])


number_of_occurrences = []

for el in final_list:
    number_of_occurrences.append(new_list.count(el))

for index in range(len(final_list)):
    print(f"{final_list[index]} -> {number_of_occurrences[index]}")