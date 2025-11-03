# this program uses a while loop to repeatedly ask the user if they want to continue
# it counts how many times the user chooses to continue and displays the total count after its done

count = 0

while True:
    answer = input("would you like to continue? (y/n): ")
    if answer.lower() == 'y':
        count += 1
    else:
        break

print(f"the loop executed {count} times.")
