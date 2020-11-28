def isOdd(num):
    if num%2==0:
        return False
    return True


def count_odd(list):
    num_of_odds = 0
    for el in list:
        if isOdd(el):
            num_of_odds+=1
    return num_of_odds


if __name__=="__main__":
    data_list = list(map(int, input().split(" ")))
    print(count_odd((data_list)))