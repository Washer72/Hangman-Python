import tkinter as tk
import random

# List of words
words = ['python', 'hangman', 'simple', 'code', 'game']

# Function to start a new game
def new_game():
    global word, guessed, wrong_guesses, game_over
    word = random.choice(words)
    guessed = ['_'] * len(word)
    wrong_guesses = 0
    game_over = False
    result_label.config(text='')
    canvas.delete('all')
    draw_gallows()
    for letter in letter_buttons:
        letter_buttons[letter].config(state='normal', fg='black')
    update_display()

# Function to update the display
def update_display():
    word_label.config(text=' '.join(guessed))
    guesses_label.config(text=f'Wrong guesses: {wrong_guesses}')
    if '_' not in guessed:
        result_label.config(text='You won!')
        end_game()
    elif wrong_guesses >= 6:
        result_label.config(text=f'You lost! The word was: {word}')
        draw_hangman()  # Complete the hangman drawing when the game is lost
        end_game()

# Function to handle a guess
def guess_letter(letter):
    global wrong_guesses
    if game_over:
        return
    if letter_buttons[letter]['state'] == 'disabled':
        return
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
        letter_buttons[letter].config(state='disabled', fg='green')
    else:
        wrong_guesses += 1
        letter_buttons[letter].config(state='disabled', fg='red')
        draw_hangman()
    update_display()

# Function to end the game
def end_game():
    global game_over
    game_over = True
    for letter in letter_buttons:
        letter_buttons[letter].config(state='disabled')

# Function to draw gallows
def draw_gallows():
    canvas.create_line(100, 20, 100, 150, width=2)  # Vertical pole
    canvas.create_line(50, 150, 150, 150, width=2)  # Base
    canvas.create_line(100, 20, 50, 20, width=2)    # Top horizontal pole
    canvas.create_line(50, 20, 50, 40, width=2)     # Rope

# Function to draw the hangman
def draw_hangman():
    if wrong_guesses == 1:
        canvas.create_oval(40, 40, 60, 60, width=2)  # Head
    elif wrong_guesses == 2:
        canvas.create_line(50, 60, 50, 100, width=2)  # Body
    elif wrong_guesses == 3:
        canvas.create_line(50, 70, 30, 90, width=2)  # Left arm
    elif wrong_guesses == 4:
        canvas.create_line(50, 70, 70, 90, width=2)  # Right arm
    elif wrong_guesses == 5:
        canvas.create_line(50, 100, 30, 130, width=2)  # Left leg
    elif wrong_guesses == 6:
        canvas.create_line(50, 100, 70, 130, width=2)  # Right leg

# Setting up the main window
root = tk.Tk()
root.title('Hangman Game')

# Display labels
word_label = tk.Label(root, font=('Helvetica', 20))
word_label.pack()

guesses_label = tk.Label(root, font=('Helvetica', 14))
guesses_label.pack()

result_label = tk.Label(root, font=('Helvetica', 14))
result_label.pack()

# Creating canvas for drawing
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
draw_gallows()

# Creating buttons for each letter
letter_buttons = {}
for letter in 'abcdefghijklmnopqrstuvwxyz':
    btn = tk.Button(root, text=letter, command=lambda l=letter: guess_letter(l))
    btn.pack(side='left')
    letter_buttons[letter] = btn

# New game button
new_game_btn = tk.Button(root, text='New Game', command=new_game)
new_game_btn.pack()

# Start a new game
new_game()

# Run the application
root.mainloop()
