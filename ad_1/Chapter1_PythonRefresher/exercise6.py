# this program prints numbers from 1 to 100
# it replaces multiples of 3 with 'fizz', multiples of 5 with 'buzz',
# and multiples of both with 'fizzbuzz'

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
