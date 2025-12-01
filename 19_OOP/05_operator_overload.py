class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        '''
        :param p: Point
        :return: Point
        '''
        return Point((self.x + p.x), ( self.y + p.y))

    # Overloading the + operator
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def info(self):
        return f"Point: {self.x}, {self.y}"

p1 = Point(3,2)
p2 = Point(6,2)

p3 = p1.sum(p2)
p4 = p1 + p2 #Overloaded
print(f"p3 = {p3.info()}")
print(f"p4 = {p4.info()}")
