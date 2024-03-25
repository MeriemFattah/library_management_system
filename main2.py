from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from members import *
from employees import *
from trainees import *
from lending import *
from data_treatment import *
from bookshelf import *
from password import *


connection = mysql.connector.connect(
    host='localhost', database='biblio', user='root', password='1236547')
cursor = connection.cursor()


def signin():
    username = user.get()
    password = code.get()
    if username == 'admin' and password == '1234':
        global screen
        screen = Toplevel(root)

        screen.title("The national library of Rabat ")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        # ne permet pas le redimensionnement de la fenetre.
        screen.resizable(False, False)
        canvas = Canvas(screen, width=925, height=500, bg='#f0f8ff')
        canvas.pack()
        img = (Image.open("photo.jpg"))
        # permet le redimensionnement de l'image et que l'image prend qu'un seul nom
        resized_image = img.resize((900, 500), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        # l'image sera positionné dans le coin supérieur gauche de l’espace disponible.
        canvas.create_image(10, 10, anchor=NW, image=new_image)
        btn0 = Button(screen, text="data treatement ",
                      bg='#f0f8ff', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=data_treatment)
        btn0.place(x=450, y=120, relwidth=0.45, relheight=0.1)
        btn1 = Button(screen, text="Employees",
                      bg='#f0f8ff', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=employees)
        btn1.place(x=450, y=160, relwidth=0.45, relheight=0.1)

        btn2 = Button(screen, text="Lending", bg='#f0f8ff',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=lending)
        btn2.place(x=450, y=200, relwidth=0.45, relheight=0.1)

        btn3 = Button(screen, text="Bookshelf",
                      bg='#f0f8ff', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=bookshelf)
        btn3.place(x=450, y=240, relwidth=0.45, relheight=0.1)

        btn4 = Button(screen, text="Trainees and Interns", bg='#f0f8ff',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=trainees)
        btn4.place(x=450, y=280, relwidth=0.45, relheight=0.1)

        btn5 = Button(screen, text="Members", bg='#f0f8ff',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=members)
        btn5.place(x=450, y=320, relwidth=0.45, relheight=0.1)
        screen.mainloop()
    elif username == 'stagiaire' and password == '20012002':
        screen = Toplevel(root)
        screen.title("The national library of Rabat ")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        # ne permet pas le redimensionnement de la fenetre.
        screen.resizable(False, False)
        canvas = Canvas(screen, width=925, height=500, bg='#f0f8ff')
        canvas.pack()
        img = (Image.open("photo.jpg"))
        # permet le redimensionnement de l'image et que l'image prend qu'un seul nom
        resized_image = img.resize((900, 500), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        # l'image sera positionné dans le coin supérieur gauche de l’espace disponible.
        canvas.create_image(10, 10, anchor=NW, image=new_image)

        btn1 = Button(screen, text=" lendings", bg='#f0f8ff',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=lending)
        btn1.place(x=450, y=200, relwidth=0.45, relheight=0.1)
        screen.mainloop()
    elif username != 'stagaire' and password != '20012002':
        messagebox.showerror('Invalid', 'invalid username and password')
    elif password != '20012002':
        messagebox.showerror('Invalid', 'invalid  password')
    elif username != 'stagiaire':
        messagebox.showerror('Invalid', 'invalid  username')
    elif username != 'admin' and password != '1234':
        messagebox.showerror('Invalid', 'invalid username and password')
    elif password != '1234':
        messagebox.showerror('Invalid', 'invalid  password')
    elif username != 'admin':
        messagebox.showerror('Invalid', 'invalid  username')


root = Tk()
root.title(" The national library of Rabat")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
canvas = Canvas(root, width=900, height=500)  # bg="#d1bea8"
canvas.pack()
img = (Image.open("image.jpg"))
resized_image = img.resize((900, 500), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(10, 10, anchor=NW, image=new_image)
heading = Label(text='WELCOME \n TO OUR LIBRARY!',
                font=('Times New Roman', 23, 'bold'))
heading.place(x=600, y=100)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(width=25, fg='black', border=2,
             bg='#f0f8ff', font=('Microsot YaHei Light ', 11))
user.place(x=650, y=250)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
# ------------------création button pasword


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(width=25, fg='black', border=2,
             bg='#f0f8ff', font=('Microsot YaHei Light ', 11), show="*")
code.place(x=650, y=300)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
# ------button sign_in
Button(width=15, pady=3, text='sign in',
       bg='#f0f8ff', fg='black', border=1, command=signin).place(x=698, y=350)
label = Button(text='did you forget your password?',
               fg='black',  font=('Times New Roman', 9), command=password)
label.place(x=680, y=400)
root.mainloop()
