
items = {}

while True:
    stock = input()
    if stock=='shopping time':
        break

    stock_splitter=stock.split(' ')
    product = stock_splitter[1]
    value = int(stock_splitter[2])

    if product in items:
        items[product]+=value
    else:
        items[product]=value

while True:
    buy = input()

    if buy == 'exam time':
        break

    buy_splitter = buy.split(" ")
    product = buy_splitter[1]
    value = int(buy_splitter[2])

    if product not in items:
        print(f"{product} doesn't exist")
    elif items[product]<=0:
        print(f"{product} out of stock")
    else:
        items[product]-=value

for el in items:
    if items[el]>0:
        print(f"{el} -> {items[el]}")#easier way