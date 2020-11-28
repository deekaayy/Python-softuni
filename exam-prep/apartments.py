apartments = {}


data_list = input().split(" -> ")

while not data_list[0] == "collectApartments":
    neighbourhood = data_list[0]
    blocks_nums = list(map(int,data_list[1].split(",")))

    if neighbourhood not in apartments.keys():
        apartments[neighbourhood] = {}
        for num in blocks_nums:
            apartments[neighbourhood][num] = {'available_apartments_count': 0, 'price': None}


    data_list = input().split(" -> ")

data_list = input().split(" -> ")

while not data_list[0] == 'report':
    neighborhood, block_num = data_list[0].split("&")
    count_available, price = list(map(int, data_list[1].split("|")))
    block_num = int(block_num)

    if neighborhood in apartments.keys() and block_num in apartments[neighborhood].keys():
        apartments[neighbourhood][block_num]["avaiable_apartments_count"] = count_available
        apartments[neighbourhood][block_num]["price"] = price0