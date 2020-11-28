nums = list(map(int, input().split(" ")))
positive_nums = list(filter(lambda x : x >= 0, nums))

if (len(positive_nums)==0):
    print("empty")
else:
    print(*list(reversed(positive_nums)))