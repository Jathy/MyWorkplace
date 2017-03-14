# utf-8
# python3.5

import tkinter as tk

window = tk.Tk()
window.title('My Win')
window.geometry('200x400')

var1 = tk.StringVar()

label = tk.Label(window, bg='yellow', width=6, textvariable=var1)
label.pack()

def print_selection():
    varlue = listbox.get(listbox.curselection())
    var1.set(varlue)

def Insert():
    varlue = entry.get()
    listbox.insert('end',varlue)
    
def Delete_selection():
    listbox.delete(listbox.curselection())

button1 = tk.Button(window, text='Print',
        width=10, height=2, command=print_selection)
button1.pack()

button2 = tk.Button(window, text='Delete',
        width=10, height=2, command=Delete_selection)
button2.pack()
# var2 = tk.StringVar()
# var2.set((11,22,33))
# listbox = tk.Listbox(window, listvariable=var2)
listbox = tk.Listbox(window)
# list_items = [1,2,3,4]
# for item in list_items:
    # listbox.insert('end',item)
# listbox.insert(1,'first')
# listbox.insert(2,'second')
# listbox.delete(2)
listbox.pack()

button3 = tk.Button(window, text='Insert',
        width=15, height=2, command=Insert)
button3.pack()

entry = tk.Entry(window, show=None)
entry.pack()

window.mainloop()
