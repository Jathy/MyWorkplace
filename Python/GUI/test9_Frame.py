# utf-8
# python 3.5

import tkinter as tk

window = tk.Tk()
window.title('My Win')
window.geometry('200x200')

tk.Label(window, text='on the window').pack()

frame = tk.Frame(window)
frame.pack()
frame_l = tk.Frame(frame, )
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='Left1').pack()
tk.Label(frame_l, text='Left2').pack()
tk.Label(frame_r, text='Right').pack()



window.mainloop()
