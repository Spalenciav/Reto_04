
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)

class Shape:
    def __init__(self, vertices=None, edges=None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []
        self.inner_angles = []
        self.is_regular = False

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

class Triangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)

    def compute_inner_angles(self):
        if len(self.vertices) == 3:
            a = self.edges[0].length
            b = self.edges[1].length
            c = self.edges[2].length
            angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
            angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
            angle_C = math.pi - angle_A - angle_B
            self.inner_angles = [angle_A, angle_B, angle_C]
        else:
            print("Invalid number of vertices for a triangle.")

class Isosceles(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.is_regular = True

class Equilateral(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.is_regular = True

class Scalene(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)

class TriRectangle(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)

class Rectangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)

    def compute_area(self):
        if len(self.vertices) == 4:
            width = min(self.edges[0].length, self.edges[1].length)
            height = max(self.edges[0].length, self.edges[1].length)
            return width * height
        else:
            print("Invalid number of vertices for a rectangle.")
            return None

    def compute_perimeter(self):
        if len(self.vertices) == 4:
            width = min(self.edges[0].length, self.edges[1].length)
            height = max(self.edges[0].length, self.edges[1].length)
            return 2 * (width + height)
        else:
            print("Invalid number of vertices for a rectangle.")
            return None

class Square(Rectangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.is_regular = True

    def compute_area(self):
        if len(self.vertices) == 4:
            side_length = self.edges[0].length
            return side_length ** 2
        else:
            print("Invalid number of vertices for a square.")
            return None

    def compute_perimeter(self):
        if len(self.vertices) == 4:
            side_length = self.edges[0].length
            return 4 * side_length
        else:
            print("Invalid number of vertices for a square.")
            return None


#Example

#Point
point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(0, 4)
point4 = Point(3, 4)

#Line
line1 = Line(point1, point2)
line2 = Line(point2, point4)
line3 = Line(point4, point3)
line4 = Line(point3, point1)

#Triangule
triangle = Triangle([point1, point2, point3], [line1, line2, line4])
triangle.compute_inner_angles()
print("Inner angles of triangle:", triangle.inner_angles)

#isosceles triangle
isosceles_triangle = Isosceles([point1, point2, point4], [line1, line2, line3])
isosceles_triangle.compute_inner_angles()
print("Isosceles triangle area:", isosceles_triangle.compute_area())

#equilateral triangle
equilateral_triangle = Equilateral([point1, point2, point3], [line1, line2, line4])
equilateral_triangle.compute_inner_angles()
print("Equilateral triangle perimeter:", equilateral_triangle.compute_perimeter())

#Scalene triangle
scalene_triangle = Scalene([point1, point2, point3], [line1, line2, line3])
scalene_triangle.compute_inner_angles()
print("Scalene triangle area:", scalene_triangle.compute_area())

#Rectangle
rectangle = Rectangle([point1, point2, point4, point3], [line1, line2, line3, line4])
print("Rectangle area:", rectangle.compute_area())
print("Rectangle perimeter:", rectangle.compute_perimeter())

#Square
square = Square([point1, point2, point4, point3], [line1, line2, line3, line4])
print("Square area:", square.compute_area())
print("Square perimeter:", square.compute_perimeter())
