def sum (list):
    temp=0
    for element in list:
        temp+=element
    return temp


if __name__=="__main__":
    #data_list = list( map(int, input().split(" ")))
    #print(sum(data_list))
    a = []
    num = int(input())
    for index in range(num):
        pushed = int(input())
        a.append(pushed)
    print(sum(a))