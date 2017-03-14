# utf-8
# python 3.5

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('200x100')

var = tk.StringVar()
on_hit = False

# label
label = tk.Label(window, textvariable=var, bg='green', font=('Arial,12'), 
        width=15, height=2)
label.pack()

# button
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

button = tk.Button(window, text='hit me', width=15,
        height=2, command=hit_me)
button.pack()


window.mainloop()
