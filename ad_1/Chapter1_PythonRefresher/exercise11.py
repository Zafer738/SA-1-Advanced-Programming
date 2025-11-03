# this program shows the tuple operations
# how it accesses elements, reverses the tuple, counts occurrences, finds index values, and prints the length..

year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

print("value at index -3:", year[-3])
print("original tuple:", year)
print("reversed tuple:", year[::-1])
print("number of times 2009 appears:", year.count(2009))
print("index of 2018:", year.index(2018))
print("length of tuple:", len(year))
