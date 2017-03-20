# utf-8
# python 3.5

import tkinter as tk
window = tk.Tk()
window.title("My Win")
window.geometry('200x200')

#-------------------pack----------------------------------
# tk.Label(window, text='top').pack(side='top')
# tk.Label(window, text='bottom').pack(side='bottom')
# tk.Label(window, text='left').pack(side='left')
# tk.Label(window, text='right').pack(side='right')

#-------------------grid----------------------------------
#for i in range(4):
#    for j in range(3):
#        # tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
#        tk.Label(window, text=1).grid(row=i, column=j, ipadx=10, ipady=10)

#-------------------place----------------------------------

tk.Label(window, text=1).place(x=10, y=100, anchor='center')

window.mainloop()
