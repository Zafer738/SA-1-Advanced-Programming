# this program prints an arrow pattern using asterisks

rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
