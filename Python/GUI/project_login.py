# utf-8
# python 3.5

import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('Welcome')
window.geometry('450x300')

canvas = tk.Canvas(window, bg='white', width=450, height=160)

# image
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(80, 0, anchor='nw', image=image_file )

canvas.pack(side='top')

# username and password

tk.Label(window, text='User name: ').place(x=80, y=180)
tk.Label(window, text='Password: ').place(x=80, y=210)

var_username = tk.StringVar()
var_password = tk.StringVar()

var_username.set('example@email.com')
entry_username = tk.Entry(window, textvariable=var_username)
entry_username.place(x=190, y=180)
            
entry_password = tk.Entry(window, show='*', textvariable=var_password)            
entry_password.place(x=190, y=210)


# login and sign

def usr_login():
    usr_name = var_username.get()
    usr_pwd = var_password.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='Nice to see ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again!')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcom',
                'You have not sign up. Sign up today?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_user():
        new_name = var_new_name.get()
        new_password = var_new_password.get()
        password_confirm = var_password_confirm.get()

        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            if new_password != password_confirm:
                tk.message.showerror('Error', 'Password and confirm password must to be same!')
            elif new_name in exist_usr_info:
                tk.messagebox.showerror('Error', 'The user has already signed up!')
            elif new_password == '':
                tk.messagebox.showerror('Error', 'The password could not be empty!')
            else:
                exist_usr_info[new_name] = new_password
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    tk.messagebox.showinfo('Success!','You have successfully signed up!')
                    window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign Up')

    var_new_name = tk.StringVar()
    var_new_name.set('example@email.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=var_new_name)
    entry_new_name.place(x=150, y=10)


    var_new_password = tk.StringVar()
    tk.Label(window_sign_up, text='New password: ').place(x=10, y=50)
    entry_new_password = tk.Entry(window_sign_up, show='*', textvariable=var_new_password)
    entry_new_password.place(x=150, y=50)

    var_password_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm Password: ').place(x=10, y=90)
    entry_password_confirm = tk.Entry(window_sign_up, show='*', textvariable=var_password_confirm)
    entry_password_confirm.place(x=150, y=90)
    
    button_confrim_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_user)
    button_confrim_sign_up.place(x=150, y=130)


button_login = tk.Button(window, text='Login', command=usr_login)
button_login.place(x=190, y=240)

button_login = tk.Button(window, text='Sign up', command=usr_sign_up)
button_login.place(x=270, y=240)

window.mainloop()
