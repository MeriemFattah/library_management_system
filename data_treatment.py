
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

connection = mysql.connector.connect(host='localhost',
                                        database='biblio',
                                        user='root',
                                        password='1236547')

cursor = connection.cursor()

def data_treatment():
    emp = Tk()
    emp.title('The national library of Rabat')
    emp.geometry('925x500+300+200')
    emp.config(bg="white")
    # ne permet pas le redimensionnement de la fenetre.
    emp.resizable(False, False)
    canvas = Canvas(emp, width=925, height=500, bg="#f0f8ff")
    canvas.pack()

    def Users4():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        name = Label(book1, text="Number :")
        name.place(x=70, y=80)

        cursor.execute(
            '''select count(n°exemp) FROM exemplaire where id_util in (select id_util from utilisateur where  type_util='abonnée'); ''')

        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('N')
        t.column('#0', width=0, stretch=NO)
        t.column('N', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('N', anchor=CENTER, text='N')
        t.place(x=70, y=160, relwidth=0.4, relheight=0.4)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users3():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        name = Label(book1, text="Names :")
        name.place(x=70, y=80)

        cursor.execute(
            '''select nom_util from utilisateur where nom_util like '%a%a%'; ''')

        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('N')
        t.column('#0', width=0, stretch=NO)
        t.column('N', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('N', anchor=CENTER, text='N')
        t.place(x=70, y=160, relwidth=0.4, relheight=0.4)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users2():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        name = Label(book1, text="Name of books :")
        name.place(x=70, y=80)

        cursor.execute(
            ''' select tit_doc from document where ref_doc in (select ref_doc from exemplaire where amende_forfait <> '0');''')

        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('N')
        t.column('#0', width=0, stretch=NO)
        t.column('N', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('N', anchor=CENTER, text='N')
        t.place(x=70, y=160, relwidth=0.4, relheight=0.4)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users1():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        name = Label(book1, text="Number of books :")
        name.place(x=70, y=80)

        cursor.execute(
            '''select count(n°exemp) from exemplaire where (type_exemp= 'en traveaux' );''')

        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('N')
        t.column('#0', width=0, stretch=NO)
        t.column('N', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('N', anchor=CENTER, text='N')
        t.place(x=70, y=160, relwidth=0.4, relheight=0.4)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users6():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        name = Label(book1, text="Number of books :")
        name.place(x=70, y=80)

        cursor.execute(
            '''select date_n_util from utilisateur order by date_n_util asc;''')

        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('N')
        t.column('#0', width=0, stretch=NO)
        t.column('N', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('N', anchor=CENTER, text='N')
        t.place(x=70, y=160, relwidth=0.4, relheight=0.4)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users5():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        cursor.execute(
            'select nom_util from utilisateur where id_util in (select id_util from exemplaire group by id_util having count(ref_doc)>=3)')
        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('Name_User')
        t.column('#0', width=0, stretch=NO)
        t.column('Name_User', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Name_User', anchor=CENTER, text='Name_User')
        t.place(x=70, y=160, relwidth=0.6, relheight=0.6)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users7():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        cursor.execute(
            '''select nom_util , date_n_util from utilisateur  where type_util='occasionnel';''')
        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('User', 'Date_birth')
        t.column('#0', width=0, stretch=NO)
        t.column('User', anchor=CENTER, width=80)
        t.column('Date_birth', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('User', anchor=CENTER, text='User')
        t.heading('Date_birth', anchor=CENTER, text='Date_birth')
        t.place(x=70, y=160, relwidth=0.6, relheight=0.6)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users8():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        cursor.execute(
            '''select nom_util , date_n_util from utilisateur where type_util='abonnée';''')
        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('User', 'Date_birth')
        t.column('#0', width=0, stretch=NO)
        t.column('User', anchor=CENTER, width=80)
        t.column('Date_birth', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('User', anchor=CENTER, text='User')
        t.heading('Date_birth', anchor=CENTER, text='Date_birth')
        t.place(x=70, y=160, relwidth=0.6, relheight=0.6)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Users9():
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        cursor.execute(
            '''select  nom_categbiblio , count(nom_biblio) from bibliothecaire group by nom_categbiblio ;''')
        a = cursor.fetchall()
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('Category', 'Number_employees')
        t.column('#0', width=0, stretch=NO)
        t.column('Category', anchor=CENTER, width=80)
        t.column('Number_employees', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Category', anchor=CENTER, text='Category')
        t.heading('Number_employees', anchor=CENTER, text='Number_employees')
        t.place(x=70, y=160, relwidth=0.6, relheight=0.6)

        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    btn1 = Button(emp, text="Users that have \n  more than 2 books ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users5)
    btn1.place(x=80, y=240, relwidth=0.25, relheight=0.1)
    btn2 = Button(emp, text="Books under construction",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users1)
    btn2.place(x=380, y=240, relwidth=0.25, relheight=0.1)
    btn3 = Button(emp, text="Books with fees",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users2)
    btn3.place(x=680, y=240, relwidth=0.25, relheight=0.1)
    btn4 = Button(emp, text="Names with 2 a or more ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users3)
    btn4.place(x=80, y=160, relwidth=0.25, relheight=0.1)
    btn5 = Button(emp, text="Number of books that are \n taken by second category ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users4)
    btn5.place(x=380, y=160, relwidth=0.25, relheight=0.1)
    btn6 = Button(emp, text=" The younger age \n  to the older age  ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users6)
    btn6.place(x=680, y=160, relwidth=0.25, relheight=0.1)

    btn7 = Button(emp, text=" Occasional users with \n their birth days",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users7)
    btn7.place(x=80, y=320, relwidth=0.25, relheight=0.1)

    btn8 = Button(emp, text="2nd category people \n with their birth days",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users8)
    btn8.place(x=380, y=320, relwidth=0.25, relheight=0.1)
    btn9 = Button(emp, text="Number of employees \n in each category",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Users9)
    btn9.place(x=680, y=320, relwidth=0.25, relheight=0.1)

    emp.mainloop()


