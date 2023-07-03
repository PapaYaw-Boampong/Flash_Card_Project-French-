BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_card = {}

import tkinter as tk
import pandas
import random

complete = 0

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    print(0)
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_bg, image=back)
    canvas.itemconfig(title, text="English", fill="white")
    eng_word = current_card["English"]
    canvas.itemconfig(word, text=eng_word, fill="white")


def update_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    current_word = current_card["French"]
    canvas.itemconfig(word, text=current_word, fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_bg, image=front)
    flip_timer = window.after(4000, flip_card)


def known():
    data_dict.remove(current_card)
    update_card()


window = tk.Tk()
window.title("Study French Flash Cards")
window.config(padx=60, pady=60, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, flip_card)
canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front = tk.PhotoImage(file="./images/card_front.png")
back = tk.PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front)
word = canvas.create_text(395, 280, text="word", font=(FONT_NAME, 40, "bold"))
title = canvas.create_text(395, 150, text=f"Title", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=0, columnspan=2)

update_card()

correct_img = tk.PhotoImage(file="./images/right.png")
wrong_img = tk.PhotoImage(file="./images/wrong.png")

correct_button = tk.Button(image=correct_img, highlightthickness=0, command=known)
correct_button.grid(row=2, column=2)

wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=update_card)
wrong_button.grid(row=2, column=1)

window.mainloop()
words_to_learn = pandas.DataFrame(data_dict)
words_to_learn.to_csv("data/words_to_learn.csv", index=False)
