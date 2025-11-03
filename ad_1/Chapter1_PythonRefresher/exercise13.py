# this program defines a function that takes a list of numbers and calculates the product of it
# it multiplies all numbers together and shows the final result

def product_of_list(values):
    product = 1
    for v in values:
        product *= v
    return product

nums = [2, 3, 4, 5]
print("list:", nums)
print("product of list items:", product_of_list(nums))
