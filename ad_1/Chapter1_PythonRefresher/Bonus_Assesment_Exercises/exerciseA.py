# this program shows the multiplication of tables from 1 to 10
# it uses nested loops to show results in a clear/clean and organized format

for i in range(1, 11):
    print(f"\nmultiplication table of: {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
