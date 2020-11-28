def find_result(num_as_string):
    sum_odd = 0
    sum_even = 0
    for char in num_as_string:
        if char=='-':
            continue
        number = int(char)

        if number % 2 == 0:
            sum_even+=number
        else:
            sum_odd +=number

    return sum_odd*sum_even


if __name__ == "__main__":
    a = input()
    print(find_result(a))