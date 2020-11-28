data_list = list(map(int, input().split(' ')))
data_list.sort()
#print(*data_list)
data_list = list(map(str, data_list))

print(' <= '.join(data_list))