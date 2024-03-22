# Reto_04
Reto # 4 de POO

# Punto 1
**Problema:** 
Create a repo with the class exercise

# Solución Parte 1:
```python

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

```

# Punto 2
**Problema:** 
The restaurant revisted
# Solución Parte 2:
```python



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total(self, quantity):
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Appetizer(MenuItem):
    def __init__(self, name, price, portion):
        super().__init__(name, price)
        self.portion = portion


class MainCourse(MenuItem):
    def __init__(self, name, price, protein):
        super().__init__(name, price)
        self.protein = protein


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def calculate_total(self):
        total = 0
        beverage_count = 0
        appetizer_count = 0
        main_course_count = 0

        for item, quantity in self.items:
            if isinstance(item, Beverage):
                beverage_count += 1
            elif isinstance(item, Appetizer):
                appetizer_count += 1
            elif isinstance(item, MainCourse):
                main_course_count += 1

            total += item.calculate_total(quantity)

        # Aplicar descuento si se pide al menos una bebida, una entrada y un plato principal
        if beverage_count >= 1 and appetizer_count >= 1 and main_course_count >= 1:
            discount = total * 0.1  
            total -= discount

        return total


class Payment:
    def __init__(self, amount, method):
        self._amount = amount
        self._method = method

    # Getters and Setters
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_method(self):
        return self._method

    def set_method(self, method):
        self._method = method

    def process_payment(self):
        if isinstance(self._method, Card):
            self._method.pay(self._amount)
        elif isinstance(self._method, Cash):
            self._method.pay(self._amount)
        else:
            print("Método de pago no válido")


class PaymentMethod:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class Card(PaymentMethod):
    def __init__(self, number, cvv):
        super().__init__()
        self._number = number
        self._cvv = cvv

    def pay(self, amount):
        print(f"Pagando {amount} con tarjeta {self._number[-4:]}")


class Cash(PaymentMethod):
    def __init__(self, amount_paid):
        super().__init__()
        self._amount_paid = amount_paid

    def pay(self, amount):
        if self._amount_paid >= amount:
            print(f"Pago realizado en efectivo. Cambio: {self._amount_paid - amount}")
        else:
            print(f"Fondos insuficientes. Faltan {amount - self._amount_paid} para completar el pago.")


if __name__ == "__main__":
    menu_items = [
        Beverage("Soda", 5000, "Regular"),
        Beverage("Cerveza", 10000, "Grande"),
        Appetizer("Nachos", 12000, "Grande"),
        Appetizer("Alitas de pollo", 15000, "12 piezas"),
        MainCourse("Hamburguesa", 20000, "Res"),
        MainCourse("Filete", 35000, "Ternera"),
        Beverage("Jugo", 6000, "Pequeño"),
        Appetizer("Ensalada César", 14000, "Individual"),
        MainCourse("Salmón a la parrilla", 30000, "Salmón"),
        MainCourse("Pasta Alfredo", 25000, "Pollo")
    ]

    order = Order()
    order.add_item(menu_items[0], 2) 
    order.add_item(menu_items[3])      
    order.add_item(menu_items[7])      

    total_bill = order.calculate_total()
    print("Total de la factura:", total_bill)

```
