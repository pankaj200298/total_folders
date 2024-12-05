# calculate area of circle and perimeter of circle

class circle :

    def __init__(self, radios ):
        self.radios = radios
        print(f"the radios of circle is : {self.radios} ")

    def area(self):
        area_of_c = 3.14 * self.radios * self.radios
        return print(f"area of circle is : {area_of_c}")

    def perimetr(self):
        perim = 2 * 3.14 * self.radios
        return print(f"perimeter of circle is : {perim}")


circle1 = circle(4)
circle1.area()
circle1.perimetr()