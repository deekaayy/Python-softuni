data_list = input().split(" ")
last_element = data_list.pop()
data_list.insert(0,last_element)
print(*data_list)

