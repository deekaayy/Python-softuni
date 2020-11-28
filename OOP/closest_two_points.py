import math as meth


class Point:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2

    def show_info(self):
        return f"{self.x}; {self.y}"

class Segment:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.distance = self.calc_distance()

    def calc_distance(self):
        return meth.sqrt(abs(((self.point_1.x - self.point_2.x) ** 2) + (self.point_1.y - self.point_2.y) ** 2))

    def show_info(self):
        return f"{self.distance:.3f}\n({self.point_1.x}, {self.point_1.y})\n({self.point_2.x}, {self.point_2.y})"


def create_point(x, y):
    point = Point(x,y)
    return point

n = int(input())
points_list = []

for row in range(n):
    x, y = list(map(int, input().split()))
    point = create_point(x, y)
    points_list.append(point)


segment_list = []

for index_1 in range(len(points_list)):
    for index_2 in range(len(points_list)):
        if not index_1 == index_2:
            segment = Segment(points_list[index_1], points_list[index_2])
            segment_list.append(segment)


for segment in sorted(segment_list, key = lambda s:s.distance):
    print(segment.show_info())
    break