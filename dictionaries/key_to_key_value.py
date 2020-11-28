search_key  = input()
value_to_be_found = input()
n=int(input())

data_dict = {}

for num in range(0, n):
    data_list=input().split(' => ')
    key = data_list[0]
    value = data_list[1].split(';')

    data_dict[key]=value


for key,value in data_dict.items():
    if search_key in key:
        print(f"{key}:")
        for el in value:
            if value_to_be_found in el:
                print(f"-{el}")