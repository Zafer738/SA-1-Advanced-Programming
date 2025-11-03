# this program is to find the sum of digits in a number

number = input("enter a number: ")
total = 0
for digit in number:
    total += int(digit)
print("the sum of digits is:", total)
