# this program is to sort a list of tuples using the lambda function

marks = [("codelab i", 67), ("web development", 75), ("codelab ii", 74), ("smartphone apps", 68), ("games development", 70), ("responsive web", 65)]

sorted_low_to_high = sorted(marks, key=lambda x: x[1])
print("sorted low to high:")
for course, mark in sorted_low_to_high:
    print(course, "-", mark)

sorted_high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)
print("\nsorted high to low:")
for course, mark in sorted_high_to_low:
    print(course, "-", mark)
