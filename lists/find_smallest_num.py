


if __name__=="__main__":
    data_list = list(map(int, input().split(" ")))
    min = data_list[0]

    for elem in data_list:
        if elem < min:
            min=elem

    print(min)