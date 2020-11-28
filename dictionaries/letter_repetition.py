data_list = input()

occ_dict = {char:data_list.count(char) for char in data_list}

for key,value in occ_dict.items():
    print(f"{key} -> {value}")