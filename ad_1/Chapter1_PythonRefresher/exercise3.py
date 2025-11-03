# this program checks if three given sides can form a valid triangle
# if valid, it also identifies whether the triangle is equilateral, isosceles, or scalene

a = float(input("enter length of side a: "))
b = float(input("enter length of side b: "))
c = float(input("enter length of side c: "))

if a + b > c and a + c > b and b + c > a:
    print("these sides form a triangle!")
    if a == b == c:
        print("it is an equilateral triangle.")
    elif a == b or b == c or a == c:
        print("it is an isosceles triangle.")
    else:
        print("it is a scalene triangle.")
else:
    print("these sides do not form a triangle.")
