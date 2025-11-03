# this program prints all even numbers from 1 to 100
# it uses the continue statement to skip over odd numbers

for i in range(1, 101):
    if i % 2 != 0:
        continue
    print(i)
