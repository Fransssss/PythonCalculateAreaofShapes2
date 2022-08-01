# Author: Fransiskus Agapa

# create a main class with shared name variable
# when a subclass then it can use the variable created from the main class
# super() - it makes it simpler to create and construct new subclass

# =========================
class SharedName:

    def __init__(self, pi, side, base):
        self.pi = pi
        self.side = side
        self.base = base


class Circle(SharedName):

    def __init__(self, pi, side, base, r):
        super().__init__(pi, side, base)
        self.r = r

    def area(self):
        return self.pi * self.r * self.r


class Ellipse(SharedName):

    def __init__(self, pi, side, base):
        super().__init__(pi, side, base)

    def area(self):
        return self.pi * self.side * self.base


class Trapezoid(SharedName):

    def __init__(self, pi, side, base, height):
        super().__init__(pi, side, base)
        self.height = height

    def area(self):
        return (self.side + self.base) * self.height / 2

# =========================


print("\n== Calculate Area ==")
print("1. Circle")
print("2. Ellipse")
print("3. Trapezoid")
print("E. Exit")
choice = input("choice: ").lower()   # make user input to lower case

place_holder = 0           # some shapes wont need all valued that are put in the parent class so put default value just to satisfy the parameter
pi_value = 3.14            # some shapes need pi value to calculate its area

while choice != 'e':
    if choice == '1':
        print("\n[ Area of Circle ]\n")
        print("Input value of half diameter(r): ", end=" ")
        try:              # in case user input is not digit / number
            r_val = int(input())
            circle = Circle(pi_value, place_holder, place_holder, r_val)
            print("\n[ The area of circle: " + str(circle.area()) + " ]")
        except ValueError:
            print("\n[ Invalid input = Digit only ]")

    elif choice == '2':
        print("\n[ Area of Ellipse ]\n")
        try:
            print("Input value of the side: ",end=" ")
            el_side = int(input())
            print("Input value of the base: ",end=" ")
            el_base = int(input())
            ellipse = Ellipse(pi_value, el_side, el_base)
            print("\n[ The area of ellipse: " + str(ellipse.area()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '3':
        print("\n[ Area of Trapezoid ]\n")
        try:
            print("Input value of the side: ", end=" ")
            t_side = int(input())
            print("Input value of the base: ", end=" ")
            t_base = int(input())
            print("Input value of the height: ", end=" ")
            t_height = int(input())
            trapezoid = Trapezoid(place_holder, t_side, t_base, t_height)
            print("\n[ The area of trapezoid: " + str(trapezoid.area()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Calculate Area ==")
    print("1. Circle")
    print("2. Ellipse")
    print("3. Trapezoid")
    print("E. Exit")
    choice = input("choice: ").lower()  # make user input to lower case

if choice == 'e':
    print("\n== Exit Program ==")


