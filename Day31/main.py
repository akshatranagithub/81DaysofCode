from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/german_words.csv')
finally:
    german_to_english_dict = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(german_to_english_dict)
    canvas.itemconfig(card_title, text='German', fill='black')
    canvas.itemconfig(card_word, text=current_card['German'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_title, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    german_to_english_dict.remove(current_card)
    data = pd.DataFrame(german_to_english_dict)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 273, text="", font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

tick_image = PhotoImage(file='images/right.png')
known_button = Button(image=tick_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
