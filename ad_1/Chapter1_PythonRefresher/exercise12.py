# this program allows the user to calculate the area of a square, circle, or triangle
# it provides a simple menu and uses separate functions for each shape

import math

def area_square():
    side = float(input("enter side length of square: "))
    print("area of square:", side * side)

def area_circle():
    radius = float(input("enter radius of circle: "))
    print("area of circle:", math.pi * radius ** 2)

def area_triangle():
    base = float(input("enter base of triangle: "))
    height = float(input("enter height of triangle: "))
    print("area of triangle:", 0.5 * base * height)

print("1: area of square")
print("2: area of circle")
print("3: area of triangle")

choice = input("enter your choice (1/2/3): ")

if choice == '1':
    area_square()
elif choice == '2':
    area_circle()
elif choice == '3':
    area_triangle()
else:
    print("invalid choice.")
