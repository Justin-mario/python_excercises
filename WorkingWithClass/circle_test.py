from circle import Circle


class CircleTest:
    c1 = Circle(1)
    c2 = Circle(5)
    c_area = c1.getArea()
    c_area2 = c2.getArea()
    print(f'area1 is {c_area} area 2 is {c_area2}')
    c_peri = c1.getPerimeter()
    c_peri2 = c2.getPerimeter()
    print(f'perimeter i is {c_peri} perimeter 2 is {c_peri2}')
