
def calculate_perimeter(l, w):
    perim = (l * 2) + (w * 2)
    return perim


def calculate_area(l, w):
    area = l * w
    print(f"Area: {area}cm squared.")


length = 14
width = 5

print(f"Perimeter: {calculate_perimeter(length, width)}cm")
calculate_area(length, width)
