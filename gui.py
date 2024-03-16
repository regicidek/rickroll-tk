from tkinter import *
from webbrowser import *

def btndef():
    print('save!')
    login=li.get()
    password=lip.get()
    print(f'login:{login}')
    print(f'password:{password}')
    if login=="qwerty" or "iloveyou" or "test" or 'guest' or 'info' or 'adm' or 'mysql' or 'user' or 'administrator ' or 'Oracle' or 'login' or '123' or '1' or '.':
        open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    if password=="qwerty" or "iloveyou" or "test" or 'guest' or 'info' or 'adm' or 'mysql' or 'user' or 'administrator ' or 'Oracle' or 'login' or '123' or '1' or "dragon" or 'pro' or '.' or '12345' or 'python' or "cpp" or 'password':
        open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')




w = Tk()
w.config(bg='darkblue')
w.geometry('223x223')
lbl = Label(text='login')
li = Entry(w, bg="blue")
lbls = Label(text='password')
lip = Entry(w, bg="blue")
lbl.pack()
li.pack()
lbls.pack()
lip.pack()
btn = Button(w,text='save',bg='blue', command=btndef)
btn.pack()
mainloop()