# utf-8
# python3.5

import tkinter as tk

window = tk.Tk()
window.title('My Win')
window.geometry('200x200')

entry = tk.Entry(window, show=None)
entry.pack()

def insert_point():
    var = entry.get()
    text.insert('insert', var)

def insert_end():
    var = entry.get()
    text.insert('end', var)

button1 = tk.Button(window, text='insert point',
        width=15, height=2, command=insert_point)
button1.pack()

button2 = tk.Button(window, text='insert end',
        width=15, height=2, command=insert_end)
button2.pack()

text = tk.Text(window, height=2)
text.pack()

window.mainloop()
