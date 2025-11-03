
# first we define the list of locations
locations = ['dubai', 'paris', 'switzerland', 'london', 'amsterdam', 'new york']

# now printing the list and its length
print("original list:", locations)
print("length of list:", len(locations))

# then printing the list in alphabetical order ( without modifying it )
print("\nlist in alphabetical order:", sorted(locations))

# show the original list again to confirm it has not changed 
print("list after using sorted():", locations)

# then print the list in reverse alphabetical order, again ( without modifying it )
print("\nlist in reverse alphabetical order:", sorted(locations, reverse=True))

#confirm again that the original list is unchanged
print("list after reverse sorted():", locations)

# using reverse() to change the list order
locations.reverse()
print("\nlist after using reverse():", locations)

# using sort() to sort the list in alphabetical order permanently
locations.sort()
print("\nlist after sort() ascending:", locations)

# using sort() to sort the list in reverse alphabetical order
locations.sort(reverse=True)
print("list after sort() descending:", locations)
