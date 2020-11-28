from textwrap import wrap

locations = int(input())
money = float(input())
counter = 0

for i in range (locations):
    data = input()
    if data.isdigit():
        counter += 1
        decoded_message = ''
        for item in wrap(data,2):
            decoded_message += chr(int(item))
        print(f"Reviewing item - {decoded_message}")

    elif data.isalpha():
        counter += 1
        print(f"Reviewing location - {data[::-1]}")

    #data = input()

print(f"{counter} reviews have been made this month. Salary: {float(money * counter):.2f}")