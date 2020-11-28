import math as meth


class Point:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2

    @staticmethod
    def calc_distance(p1, p2):
        return meth.sqrt(abs(((p1.x - p2.x) ** 2) + (p1.y - p2.y) ** 2))


class Box:
    def __init__(self, upper_left = Point, upper_right = Point, lower_left = Point, lower_right = Point):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.lower_left = lower_left
        self.lower_right = lower_right

    def get_width(self):
        width = Point.calc_distance(self.upper_left, self.upper_right)
        return width

    def get_height(self):
        height = Point.calc_distance(self.upper_left, self.lower_left)
        return height

    def calc_per(self):
        return self.get_height() * 2 + self.get_width() * 2

    def calc_area(self):
        return self.get_width() * self.get_height()

    def show_info(self):
        return f"Box: {self.get_width():.0f}, {self.get_height():.0f}\nPerimeter: {self.calc_per():.0f}\nArea: {self.calc_area():.0f}"


def create_point(coord):
    x, y = [int(num) for num in coord.split(":")]
    point = Point(x,y)
    return point

def create_box(u_l, u_r, b_l, b_r):
    upper_left = create_point(u_l)
    upper_right = create_point(u_r)
    bottorm_left = create_point(b_l)
    bottom_right = create_point(b_r)

    box = Box(upper_left, upper_right, bottorm_left, bottom_right)
    return box

data_list = input().split(" | ")
box_list = []

while not data_list[0] == "end":
    box = create_box(data_list[0], data_list[1], data_list[2], data_list[3])
    box_list.append(box)

    data_list = input().split(" | ")

for box in box_list:
    print(box.show_info())