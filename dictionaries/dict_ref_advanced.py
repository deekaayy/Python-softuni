data_list = list(input().split(" -> "))
base = {}

while not data_list[0] == "end":
    key = data_list[0]
    value = data_list[1]

    for el in data_list[1]:
        if el[0].isdigit():
            if key in base.keys():
                base[key] = base[key] + ", " + value
                break
            else:
                base[key]=value
                break
        elif el[0].isalpha():
            if value in base.keys():
                base[key] = base[value]
                break
            else:
                break
        break
    data_list = list(input().split(" -> "))

for key,value in base.items():
    print(f"{key} === {value}")