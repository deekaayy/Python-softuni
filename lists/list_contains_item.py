data_list = list(map(int, input().split()))
searched_item = int(input())
is_found = False

for item in data_list:
    if item == searched_item:
        is_found = True
        break

if is_found:
    print("yes")
else:
    print("no")