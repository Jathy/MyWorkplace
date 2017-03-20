# utf-8
# python3.5

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('My Win')
window.geometry('200x200')

def hit_me():
    # tk.messagebox.showinfo(title='???', message='To die or not to die?')
    # tk.messagebox.showwarning(title='???', message='To die or not to die?')
    # tk.messagebox.showerror(title='???', message='To die or not to die?')
    print(tk.messagebox.askquestion(title='???', message='To die or not to die?')) # return yes or no
    print(tk.messagebox.askyesno(title='???', message='To die or not to die?')) # return true or false
    print(tk.messagebox.askretrycancel(title='???', message='To die or not to die?')) # return true or false
    print(tk.messagebox.askokcancel(title='???', message='To die or not to die?')) # return true or false
    print(tk.messagebox.askyesnocancel(title='???', message='To die or not to die?')) # return true or false, none


tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
