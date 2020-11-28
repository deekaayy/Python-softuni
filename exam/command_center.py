input_list = list(map(int, input().split()))

commands_list = []

data = input().split()
while not data[0] == 'END':
    commands_list.extend(data)
    data = input().split()

for index in range(len(commands_list)):
    if commands_list[index] == "multiply":
        if commands_list[index + 1] == "list":
            num = int(commands_list[index+2])
            new_list = input_list * num
            input_list = new_list.copy()
        else:
            temp_list = list(commands_list[index].split())
            for i in range(len(input_list)):
                if input_list[i] == int(temp_list[1]):
                    input_list[i] = input_list[i] * int(temp_list[2])

    elif commands_list[index].__contains__("contains"):
        temp = commands_list[index].replace("contains", "")
        temp.strip()
        if int(temp) in input_list:
            print(True)
        else:
            print(False)

    elif commands_list[index] == "add":
        temp = commands_list[index].replace("add", "")
        temp.strip()
        input_list = list(map(int, input_list.extend(temp)))

input_list.sort()
print(*input_list)