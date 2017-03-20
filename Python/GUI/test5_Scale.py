# utf-8
# python 3.5

import tkinter as tk

window = tk.Tk()
window.title('My Win')
window.geometry('200x200')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

def print_selection(var):
    label.config(text='you have selected ' + var)

scale = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
        length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
scale.pack()

window.mainloop()
