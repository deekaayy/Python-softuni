data_list = list(map(float, input().split(' ')))

i = 0 #who doesn't love 'i'

while i < len(data_list) - 1:
    sum = 0

    if data_list[i]==data_list[i+1]:
        sum = data_list[i] + data_list[i+1]
        data_list[i]=sum
        data_list.remove(data_list[i+1])

        if i>0:
            i-=1
    else:
        i+=1

print(*data_list)


