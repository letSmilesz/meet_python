# class Fruit:
#     pass

# a = Fruit()
# b = Fruit()

# a.name = 'apple'
# a.weight = 120

# b.name = 'orange'
# b.weight = 150

# print(a.name, b.name)
# print(a.weight, b.weight)

# b.weight = 50

# print(a.name, b.name)
# print(a.weight, b.weight)
#-----------------------------------
# class Hello:
#     def hello_world(self):
#         print('Hello world!')

#     def greeting(self, name):
#         print(f'Helllo, {name}!')

# greet = Hello()
# greet.hello_world()
# greet.greeting('Misha')
#----------------------------------------------------------------------
# class Car:
#     def __init__(self, color):
#         self.engine_on = False
#         self.color = color
        
#     def start_stop(self, bool):
#         self.engine_on = bool

#     def drive_to(self, city):
#         if self.engine_on: print(f'Go to {city} on {self.color} car')
#         else: print('Start engine!')

# c = Car('blue')
# c.start_stop(True)
# c.drive_to('Sochi')
#-------------------------------------------------
# def f(x, y):
#     return x + y

# print(f(1, 2))
# print(f('1.2', '2.3'))

# class Books:
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author

#     def get_name(self):
#         return self.name

#     def get_author(self):
#         return self.author

# book = Books('War and piece', 'Tolstoy')
# print(f'Book is "{book.get_name()}"')
# print(f'Author is "{book.get_author()}"')
#----------------------------------------------
# from math import pi

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * pi * self.radius

# class Square:
#     def __init__(self, side) -> None:
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return self.side * 4


# def print_shape_info(shape):
#     print(f'Area = {shape.area():.3f}, perimeter = {shape.perimeter():.3f}')

# square = Square(4)
# circle = Circle(3)

# print_shape_info(circle)
# print_shape_info(square)
#--------------------------------------------------------------------------------

class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
    
    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s %= 60
        return Time(m, s)

    def info(self):
        return f'{self.minutes}:{self.seconds}'

    def __str__(self):
        return f'{self.minutes}:{self.seconds}'

t1 = Time(5, 50)
print(t1.info())
print(t1)

t2 = Time(3, 20)
print(t2.info())
print(t2)

t3 = t1 + t2
print(t3.info())
print(t3)