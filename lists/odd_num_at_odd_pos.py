def count_odd(data_list):
    odd_numb = 0
    odd_index_list = []
    for index in range(len(data_list)):
        if index % 2 == 1:
            if data_list[index] % 2 == 1:
                odd_numb += 1
                odd_index_list.append(index)

    for el in range(odd_numb):
        print(f"Index {odd_index_list[el]} -> {data_list[odd_index_list[el]]} ")


if __name__ == "__main__":
    data = list(map(int, input().split(" ")))

    count_odd(data)