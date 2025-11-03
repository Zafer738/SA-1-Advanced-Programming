
# making a simple word guessing game 

import tkinter as tk
from tkinter import ttk
import random

# here the list of words used for the game
words = ['python', 'banana', 'creative', 'computer', 'university']

# create the main window, the window size ect..
root = tk.Tk()
root.title('guess the word')
root.geometry('420x220')
root.configure(padx=10, pady=10)

# set the variables to calculate score, like guessing one word gives 5 points ect... and setting the current round
score = 0
rounds = 0
current_word = ''  # this contains the correct word for the current round
shuffled_word = tk.StringVar(value='')  # shuffles the letters
entry_var = tk.StringVar(value='')  # where the user types their guess
score_var = tk.StringVar(value='score: 0')  # the score 

# uhere's the layout for shuffled word label, entry for guess, result label, score label
word_label = tk.Label(root, textvariable=shuffled_word, font=('arial', 16))
word_label.pack(pady=10)

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

result_label = tk.Label(root, text='')
result_label.pack(pady=6)

score_label = tk.Label(root, textvariable=score_var)
score_label.pack()

# then it starts a new round by choosing a random word and shuffling its letters
def new_round():
    global current_word, rounds
    current_word = random.choice(words)  # picks a random word from the list
    shuffled = list(current_word)  # then it split into different characters
    random.shuffle(shuffled)  # shuffles the characters 
    shuffled_word.set(' '.join(shuffled))  # join with spaces for readability
    entry_var.set('')  
    result_label.config(text='')  # clear previous result 
    rounds += 1  # round counter

# check the user's guess against the "current_word" that we created earlier and updates the score
def check_guess():
    global score
    guess = entry_var.get().strip().lower()  # normalize guess for case-insensitive compare
    if guess == current_word:
        score += 1
        result_label.config(text='correct!')
    else:
        result_label.config(text=f'wrong — correct word was: {current_word}')
    score_var.set(f'score: {score}')  # updating the display of the score
    # after showing the result, it automatically start a new round after a small delay of 1200 ms
    root.after(1200, new_round)

check_btn = tk.Button(root, text='check', command=check_guess)
check_btn.pack(pady=6)

new_round()  #sets up the first round again

# run the program
root.mainloop()
