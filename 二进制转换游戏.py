import tkinter
from tkinter import Tk, Label, Frame, Button
import random

top = Tk()
top.geometry("600x200")
top.title("二进制转换游戏")

def detect():
    global target, num, score_int, score_label, time_remaining_int
    if target == num:
        target = random.randint(0, 511)
        r_num.config(text=f"给出数字为:{target}")
        score_int += 1
        score_label["text"] = f"得分：{score_int}"
        time_remaining_int += 7
        for i in button_b:
            button_b[i].default = False
            i.config(background="white")
            num = 0
            num_l["text"] = str(num).rjust(3, '0')

def countdown():
    global score_int, score_label, time_remaining_int
    time_remaining_label["text"] = f"剩余时间：{time_remaining_int}"
    if time_remaining_int > 0:
        time_remaining_int -= 1
        top.after(1000, countdown)
    else:
        time_remaining_label["text"] = "完毕"
        time_remaining_int = 15
        score_int -= 2
        score_label["text"] = f"得分：{score_int}"
        countdown()
        detect()


class TrueFalse:
    def __init__(self, button: tkinter.Button):
        self.default = False
        self.button = button
    def main(self):
        global num
        self.default = not self.default
        if self.default:
            self.button.config(background="lime")
            num += int(self.button.cget("text"))
            num_l.config(text=str(num).rjust(3, '0'))
        else:
            self.button.config(background="white")
            num -= int(self.button.cget("text"))
            num_l.config(text=str(num).rjust(3, '0'))


top.grid_columnconfigure(0, weight=1)
a1 = Frame(top)
a1.grid(row=2, column=0)

target = random.randint(0, 511)
r_num = Label(top, text=f"给出数字为:{target}", font=("times", 14))
r_num.grid(row=1, column=0)
Button(top, text="提交", command=detect).grid(row=3, column=0, pady=10, padx=100, sticky="ne")

time_remaining_int = 15
time_remaining_label = Label(top, text=f"剩余时间：{time_remaining_int}")
time_remaining_label.grid(row=3, column=0)
countdown()

score_int = 0
score_label = Label(top, text=f"得分：{score_int}")
score_label.grid(row=0, column=0, sticky="nw")

index = 0
column = 16
button_b = {}
while index <= 8:
    button = Button(a1, text=f"{2 ** index}",font=("times", 14),  background="white", width=3)
    a2 = TrueFalse(button)
    button.config(command=a2.main)
    button.grid(row=0, column=column)
    button_b[button] = a2

    if column == 16:
        Label(a1, text="=").grid(row=0, column=column + 1)
    else:
        Label(a1, text="+").grid(row=0, column=column + 1)

    index += 1
    column -= 2

num = 0
num_l = Label(a1, text=str(num).rjust(3, '0'), font=("times", 14))
num_l.grid(row=0, column=18)

top.mainloop()