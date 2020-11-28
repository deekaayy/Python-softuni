def calculate_area(base, height):
    return (base*height)/2


if __name__=="__main__":
    base_of_triangle=float(input())
    heigh_of_triangle=float(input())
    area_of_triangle=calculate_area(base_of_triangle, heigh_of_triangle)
    print(f"{area_of_triangle:.12g}")