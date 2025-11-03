# this program counts how many times each item appears in a list

staff = ["arshiya", "usman", "iftikhar", "usman", "rafia", "mary", "anmol", "zainab", "iftikhar", "arshiya", "rafia", "jake"]
count_dict = {}
for name in staff:
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

# then to show how much time each name appears
print("number of times each name appears:")
for key, value in count_dict.items():
    print(key, ":", value)
