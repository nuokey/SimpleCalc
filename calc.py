from tkinter import *

def plus_entered():
    n_1 = int(first_number.get())
    n_2 = int(second_number.get())
    answer['text'] = str(n_1 + n_2)

def minus_entered():
    n_1 = int(first_number.get())
    n_2 = int(second_number.get())
    answer['text'] = str(n_1 - n_2)

def multiplication_entered():
    n_1 = int(first_number.get())
    n_2 = int(second_number.get())
    answer['text'] = str(n_1 * n_2)

def division_entered():
    n_1 = int(first_number.get())
    n_2 = int(second_number.get())
    answer['text'] = str(n_1 / n_2)


window = Tk()
window.geometry('180x320')

first_number = Entry(bg = 'grey', fg = 'white')
first_number.place(x = 0, y = 0, width = 180, height = 30)

second_number = Entry(bg = 'grey', fg = 'white')
second_number.place(x = 0, y = 50, width = 180, height = 30)

plus = Button(text = "+", command = plus_entered, bg = 'grey', fg = 'white')
plus.place(x = 0, y = 100, width = 30, height = 30)

minus = Button(text = "-", command = minus_entered, bg = 'grey', fg = 'white')
minus.place(x = 50, y = 100, width = 30, height = 30)

multiplication = Button(text = "*", command = multiplication_entered, bg = 'grey', fg = 'white')
multiplication.place(x = 100, y = 100, width = 30, height = 30)

division = Button(text = "/", command = division_entered, bg = 'grey', fg = 'white')
division.place(x = 150, y = 100, width = 30, height = 30)

answer = Label(text = "Ответ")
answer.place(x = 0, y = 150, width = 180, height = 170)

window.mainloop()