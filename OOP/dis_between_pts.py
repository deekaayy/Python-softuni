#pepegaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
import math as meth


class Point:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2


def calc_distance(p1, p2):
    return meth.sqrt(abs(((p1.x - p2.x) ** 2) + (p1.y - p2.y) ** 2))

def create_point(x, y):
    point = Point(x,y)
    return point

x_1, y_1 = list(map(int, input().split()))
x_2, y_2 = list(map(int, input().split()))

point_1 = create_point(x_1, y_1)
point_2 = create_point(x_2, y_2)

distance = calc_distance(point_1, point_2)

print(f"{distance:.3f}")

