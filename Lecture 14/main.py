# class Student:
#     is_active = True
#     score = 0
#
# student1 = Student()

# student1.is_active = False
# student1.score = 55
# student1.email = "test@gmail.com"

# print(student1.is_active)
# print(student1.score)
# print(student1.email)

# print(Student.score)

class Student:
    is_active = True
    score = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

student1 = Student("Bob", "Smith")

print(student1.fname, student1.lname)

# class Student:
#
#     quantity = 0
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         Student.quantity += 1
#
#     def get_email(self):
#         return f"{self.fname}_{self.lname}@gmail.com"
#
#     def exam_status(self, bool):
#         if bool == True:
#             return f"{self.fname} {self.lname} passed the exam"
#         return f"{self.fname} {self.lname} did not pass the exam"
#
#
# student1 = Student("Bob", "Smith")
# student2 = Student("Alice", "White")

# print(student1.get_email())
# print(student2.get_email())

# print(Student.quantity)

# print(student1.exam_status(True))
# print(student2.exam_status(True))
# print(student1.exam_status(False))
# print(student1.exam_status("olga"))
# print(student1.exam_status(1))


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         print(f"Speed is now {self.speed}")
#
#     def slow_down(self, s):
#         if s <= self.speed:
#             self.speed -= s
#             print(f"Speed is now {self.speed}")
#         else:
#             print("Speed is less than you entered")
#
#     def brake(self):
#         self.speed = 0
#         print("You stopped the vehicle")


# class Suv(Vehicle):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#
#     def offroading(self):
#         print(f"{self.make} {self.model} can offroading")
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#
#     def take_container(self):
#         print(f"{self.make} {self.model} takes container")


# suv1 = Suv("Honda", "CRV", 2002)
# truck = Truck("Vovlo", "TDX", 2020)

# print(suv1.speed)

# suv1.accelerate(20)
# suv1.accelerate(20)
# suv1.accelerate(10)
# suv1.slow_down(15)
# suv1.slow_down(15)
# suv1.brake()
# suv1.offroading()

# truck.accelerate(20)
# truck.accelerate(20)
# truck.accelerate(10)
# truck.slow_down(15)
# truck.slow_down(15)
# truck.brake()
# truck.take_container()


# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#
#     def calculate_area(self):
#         return f"Rectangle area is {super().calculate_area()}"
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def calculate_area(self):
#         return f"Square area is {self.side * self.side}"
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base, height)
#
#     def calculate_area(self):
#         return f"Triangle area is {super().calculate_area()/2}"



# rect = Rectangle(5, 8)
# print(rect.calculate_area())

# square = Square(5)
# print(square.calculate_area())

# triangle = Triangle(10, 5)
# print(triangle.calculate_area())