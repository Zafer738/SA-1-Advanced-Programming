# this program prints a simple number pattern using nested loops
# it increases the number of printed values with each line

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
