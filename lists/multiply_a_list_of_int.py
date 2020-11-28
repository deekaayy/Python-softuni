def multiply(val, n):
    return val*n


if __name__=="__main__":
    data_list = list( map(int, input().split(" ")))
    p = int(input())
    a = [multiply(element, p) for element in data_list ]
    print(" ".join(map(str,a)))