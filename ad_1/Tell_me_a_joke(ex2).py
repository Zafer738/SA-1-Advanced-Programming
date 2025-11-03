import random    # to select a random joke from the list
import os        

# creating the function: loadJokes
# so here is what this does : -->
# it reads all jokes from the provided text file
# each joke as a (setup or punchline) tuple in a list.

def loadJokes(filename):
    jokes = []  # make an empty list to store jokes


    if not os.path.exists(filename):
        print("Error: Jokes file not found.")
        return jokes

    # open the text file and read line by line
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  
            if "?" in line:  # to make sure there is a question mark which splits the line because the joke has 2 parts 
                # the split at the first "?" only. because setups may contain multiple words
                parts = line.split("?", 1)
                setup = parts[0].strip() + "?"     
                punchline = parts[1].strip()       
                jokes.append((setup, punchline))   # store as a tuple
    return jokes

# next function is : getRandomJoke
# it selects and returns one random joke from the list.
# as we created jokes (list), which is a list of (setup, punchline) tuples
# so it gives us one single joke tuple from the given file


def getRandomJoke(jokes):
    return random.choice(jokes) if jokes else None


# next up is the function: tellJoke
# it the joke to the user in two parts:
#1. first it prints/displays the question
#2. then it Waits for user to press Enter or the user can type whast they might think would be the answer to the joke
#3. at last it finally displays the joke or punchline

def tellJoke(joke):
    setup, punchline = joke  #unpack the tuple
    print("\n" + "-" * 50)
    print(f"Alexa 🤖: {setup}")  #display the question
    input("\nPress Enter to hear the punchline...")  #here's the waiting message... user can input too
    print(f"\n😂 {punchline}")  #finally revealing the punchline with emoji
    print("-" * 50 + "\n")


# now here's the main function
# it Loads jokes from file
# waits for the user to type something
# then responds or you can say it displays the joke/punchline
# it continues untilt hew user quits

def main():
    # loads all jokes from the text file
    jokes = loadJokes("randomJokes.txt")
    if not jokes:  
        return

    print("Welcome! Type 'Alexa tell me a joke' or 'quit' to exit.\n")
    
    #it keeps looping until the user decides to quit
    while True:
        user_input = input("You: ").strip().lower()  

        #the option for the user to ask Alexa for a joke
        if user_input == "alexa tell me a joke":
            joke = getRandomJoke(jokes)  #pick a random joke
            tellJoke(joke)               

        # when the user wants to exit the program
        elif user_input in ["quit", "exit", "stop"]:
            print("\nAlexa 🤖: Goodbye! Have a great day!\n")
            break

        #if the user wants to type something else, out of context
        else:
            print("Alexa 🤖: Sorry, I only tell jokes! Try 'Alexa tell me a joke'.\n")


#to run the program
if __name__ == "__main__":
    main()
