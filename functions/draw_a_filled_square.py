def draw_lines(n):
    print('-' * 2 * n, end='')
    print()


def second(n):
    for i in range(n-2,0,-1):
        print('-', end='')
        for j in range(n - 1):
            print('\\/', end='')
        print('-', end='')
        print('')


if __name__ == "__main__":
    num = int(input())
    draw_lines(num)
    second(num)
    draw_lines(num)