# utf-8
# python 3.5

import tkinter as tk

window = tk.Tk()
window.title('My Win')
window.geometry('200x200')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love Python only')
    elif (var1.get() == 0) & (var2.get() == 1):
        label.config(text='I love C++ only')
    elif (var1.get() == 1) & (var2.get() == 1):
        label.config(text='I love both')
    else:
        label.config(text='I do not love either')
    


cb1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
        command=print_selection)
cb2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
        command=print_selection)
cb1.pack()
cb2.pack()


window.mainloop()
