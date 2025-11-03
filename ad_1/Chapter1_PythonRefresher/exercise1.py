# this program asks the user for their name and age, then greets the user. also it tells them how many characters are in their name and what would be their age next year
print("hello, user!")
name = input("what is your name?\n")
age = int(input("what is your age?\n"))

print(f"it is good to meet you, {name.title()}")
print("the length of your name is:")
print(len(name))
print(f"you will be {age + 1} in a year.")
