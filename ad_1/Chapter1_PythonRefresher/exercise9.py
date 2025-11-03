# this program creates a list of integers and performs several list operations
# it prints the list, finds the highest value and lowest value, and it sorts the list and adds new elements at the end

numbers = [12, 45, 23, 67, 89, 34, 22, 90, 11, 56]

print("list elements:")
for num in numbers:
    print(num, end=' ')
print("\n")

print("highest value:", max(numbers))
print("lowest value:", min(numbers))

numbers.sort()
print("sorted ascending:", numbers)

numbers.sort(reverse=True)
print("sorted descending:", numbers)

numbers.append(100)
numbers.append(200)
print("list after appending:", numbers)
