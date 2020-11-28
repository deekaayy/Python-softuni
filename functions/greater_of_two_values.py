def compare_int(num1, num2):
    return max(num1,num2)


def compare_char(char1, char2):
    return max(char1,char2)


def compare_string(str1, str2):
    if str1 > str2:
        return str1
    else:
        return str2


def compare(type):
    if type=="int":
        x=int(input())
        y=int(input())
        return compare_int(x,y)
    elif type=="char":
        x=input()
        y=input()
        return compare_char(x,y)
    elif type=="string":
        x=input()
        y=input()
        return compare_string(x,y)


if __name__=="__main__":
    type = input()
    print(compare(type))