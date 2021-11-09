from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Screen
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label_timer.grid(column=1, row=0)

# Canvas with tomato img and timer counter text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Volumes/Extreme SSD/Python Bootcamp/Day 28/Mac/pomodoro_project/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Button start
def start_timer():
    pass


button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)


def reset_timer():
    pass


button_reset = Button(text="Stop", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

# Check label
label_check = Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN)
label_check.grid(column=1, row=3)

window.mainloop()
