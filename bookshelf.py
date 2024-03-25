
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from ecrire import *

connection = mysql.connector.connect(host='localhost',
                                        database='biblio',
                                        user='root',
                                        password='123654789')

cursor = connection.cursor()


def bookshelf():

    book = Tk()
    book.title("The national library of Rabat ")
    book.geometry('925x500+300+200')
    book.config(bg="#d1bea8")
    book.resizable(False, False)
    canvas = Canvas(book, width=925, height=500, bg="#f0f8ff")
    canvas.pack()

    def periodique():
        per = Tk()
        per.title("The national library of Rabat ")
        per.geometry('925x500+300+200')
        per.config(bg="#d1bea8")
        per.resizable(False, False)
        canvas = Canvas(per, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        def on_enter(e):
            user1.delete(0, 'end')

        def on_leave(e):
            name = user1.get()
            if name == '':
                user1.insert(0, 'ISSN_periodique')

        user1 = Entry(per, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user1.place(x=70, y=80)
        user1.insert(0, "ISSN_periodique")
        user1.bind('<FocusIn>', on_enter)
        user1.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user2.delete(0, 'end')

        def on_leave(e):
            name = user2.get()
            if name == '':
                user2.insert(0, 'volume of periodique')

        user2 = Entry(per, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user2.place(x=70, y=120)
        user2.insert(0, "volume of periodique")
        user2.bind('<FocusIn>', on_enter)
        user2.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user3.delete(0, 'end')

        def on_leave(e):
            name = user3.get()
            if name == '':
                user3.insert(0, 'reference of document')

        user3 = Entry(per, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user3.place(x=350, y=80)
        user3.insert(0, "reference of document")
        user3.bind('<FocusIn>', on_enter)
        user3.bind('<FocusOut>', on_leave)

        def Delete():
            sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
            sql = """Delete from periodique where code_issn_per = {}""".format(
                user1.get())
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql1)
            cursor.execute(sql)
            cursor.execute(sql2)
            selected_item1 = t.selection()[0]
            t.delete(selected_item1)
            connection.commit()

        def Exit():
            per.destroy()

        def select():
            cursor.execute(
                """ select * from periodique where code_issn_per={};""".format(user1.get()))
            a = cursor.fetchall()
            for x in a:
                user1.delete(0, END)
                user1.insert(END, x[0])
                user2.delete(0, END)
                user2.insert(END, x[1])
                user3.delete(0, END)
                user3.insert(END, x[2])
            connection.commit()

        def update():
            sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
            cursor.execute(sql1)
            sql = """ update periodique set vol_per ={},ref_doc={} where code_issn_per={};""".format(
                user2.get(), user3.get(), user1.get())
            cursor.execute(sql)
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql2)
            selected_item = t.selection()[0]
            t.item(selected_item, text="blub", values=(
                user1.get(), user2.get(), user3.get()))
            connection.commit()

        def Reset():
            decision = messagebox.askquestion(
                "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
            if decision != 'yes':
                return
            else:
                sql = """SET FOREIGN_KEY_CHECKS=0 """
                sql1 = """DELETE FROM periodique """
                sql3 = """SET FOREIGN_KEY_CHECKS=1"""
                cursor.execute(sql)
                cursor.execute(sql1)
                cursor.execute(sql3)
                for item in t.get_children():
                    t.delete(item)
                connection.commit()

        def insert():
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            cursor.execute(sql)
            mySql_insert_query = '''INSERT INTO periodique(code_issn_per,vol_per,ref_doc) VALUES({},{},{})'''.format(
                user1.get(), user2.get(), user3.get())

            cursor.execute(mySql_insert_query)
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql3)
            val = (user1.get(), user2.get(), user3.get())
            t.insert(parent='', index=val[0],
                     iid=val[0], text='', values=val)
            connection.commit()

        btn1 = Button(per, text="Add ",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
        btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

        btn2 = Button(per, text=" Update", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
        btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

        btn3 = Button(per, text="Search",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
        btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

        btn4 = Button(per, text="Delete", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
        btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

        btn5 = Button(per, text="Reset", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
        btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
        btn6 = Button(per, text="Exit", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
        btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)

        t = ttk.Treeview(per, height=5)
        t['columns'] = ('code_issn_per', 'vol_per', 'ref_doc')
        t.column('#0', width=0, stretch=NO)
        t.column('code_issn_per', anchor=CENTER, width=80)
        t.column('vol_per', anchor=CENTER, width=80)
        t.column('ref_doc', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('code_issn_per', anchor=CENTER, text='code_issn_per')
        t.heading('vol_per', anchor=CENTER, text='vol_per')
        t.heading('ref_doc', anchor=CENTER, text='ref_doc')
        t.place(x=70, y=230, relwidth=0.6, relheight=0.4)

        # query to retrieve details from books table

        connection = mysql.connector.connect(host='localhost',
                                             database='biblio',
                                             user='root',
                                             password='1236547')

        cursor = connection.cursor()
        # set variable in query
        cursor.execute('select * from periodique ')
        # fetch result
        record = cursor.fetchall()

        for i in record:
            t.insert(parent='', index=i[0], iid=i[0], text='', values=i)

        per.mainloop()

    def livre():
        livre = Toplevel(book)
        livre.title("The national library of Rabat ")
        livre.geometry('925x500+300+200')

        livre.resizable(False, False)
        canvas = Canvas(livre, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        def Exit():
            livre.destroy()

        def insert():
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            cursor.execute(sql)
            mySql_insert_query = '''INSERT INTO livre(code_isbn_liv,ref_doc) VALUES({},{})'''.format(
                user1.get(), user2.get())
            cursor.execute(mySql_insert_query)
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql3)
            val = (user1.get(), user2.get())
            tree2.insert(parent='', index=val[0],
                         iid=val[0], text='', values=val)
            connection.commit()

        def Delete():
            sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
            sql = """Delete from livre where code_isbn_liv = {}""".format(
                user1.get())
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql1)
            cursor.execute(sql)
            cursor.execute(sql2)
            selected_item1 = tree2.selection()
            tree2.delete(selected_item1[0])
            connection.commit()

        def select():
            cursor.execute(
                """ select * from livre where code_isbn_liv={}""".format(user1.get()))
            a = cursor.fetchall()
            for x in a:
                user1.delete(0, END)
                user1.insert(END, x[0])
                user2.delete(0, END)
                user2.insert(END, x[1])
            connection.commit()
        btn1 = Button(livre, text="Add ",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
        btn1.place(x=680, y=140, relwidth=0.25, relheight=0.1)
        btn2 = Button(livre, text="Search",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
        btn2.place(x=680, y=200, relwidth=0.25, relheight=0.1)

        btn3 = Button(livre, text="Delete", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
        btn3.place(x=680, y=260, relwidth=0.25, relheight=0.1)

        btn4 = Button(livre, text="Exit", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
        btn4.place(x=680, y=320, relwidth=0.25, relheight=0.1)

        def on_enter(e):
            user1.delete(0, 'end')

        def on_leave(e):
            name = user1.get()
            if name == '':
                user1.insert(0, 'code_isbn_liv')

        user1 = Entry(livre, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user1.place(x=70, y=60)
        user1.insert(0, "code_isbn_liv")
        user1.bind('<FocusIn>', on_enter)
        user1.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user2.delete(0, 'end')

        def on_leave(e):
            name = user2.get()
            if name == '':
                user2.insert(0, 'ref_doc')

        user2 = Entry(livre, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user2.place(x=300, y=60)
        user2.insert(0, "ref_doc")
        user2.bind('<FocusIn>', on_enter)
        user2.bind('<FocusOut>', on_leave)

        tree2 = ttk.Treeview(livre, height=5)
        tree2['columns'] = ('code_isbn_liv', 'ref_doc')
        tree2.column('#0', width=0, stretch=NO)
        tree2.column('code_isbn_liv', anchor=CENTER, width=80)
        tree2.column('ref_doc', anchor=CENTER, width=80)

        tree2.heading('#0', anchor=CENTER, text='')
        tree2.heading('code_isbn_liv', anchor=CENTER, text='code_isbn_liv')
        tree2.heading('ref_doc', anchor=CENTER, text='ref_doc')

        tree2.place(x=70, y=140, relwidth=0.6, relheight=0.4)

    # query to retrieve details from books table

        connection = mysql.connector.connect(host='localhost',
                                             database='biblio',
                                             user='root',
                                             password='123654789')

        cursor = connection.cursor()
        # set variable in query
        cursor.execute('select * from livre')
        # fetch result
        record = cursor.fetchall()

        for i in record:
            tree2.insert(parent='', index=i[0], iid=i[0], text='', values=i)
        livre.mainloop()

    def auteur():
        aut = Tk()
        aut.title("The national library of Rabat ")
        aut.geometry('925x500+300+200')
        aut.config(bg="#d1bea8")
        aut.resizable(False, False)
        canvas = Canvas(aut, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        def on_enter(e):
            user1.delete(0, 'end')

        def on_leave(e):
            name = user1.get()
            if name == '':
                user1.insert(0, 'Identifier of Author')

        user1 = Entry(aut, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user1.place(x=70, y=120)
        user1.insert(0, "Identifier of Author")
        user1.bind('<FocusIn>', on_enter)
        user1.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user2.delete(0, 'end')

        def on_leave(e):
            name = user2.get()
            if name == '':
                user2.insert(0, ' Last Name of Author')

        user2 = Entry(aut, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user2.place(x=70, y=160)
        user2.insert(0, "Last Name of Author")
        user2.bind('<FocusIn>', on_enter)
        user2.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user3.delete(0, 'end')

        def on_leave(e):
            name = user3.get()
            if name == '':
                user3.insert(0, 'First Name Of Author')

        user3 = Entry(aut, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user3.place(x=350, y=120)
        user3.insert(0, "First Name Of Author")
        user3.bind('<FocusIn>', on_enter)
        user3.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user4.delete(0, 'end')

        def on_leave(e):
            name = user4.get()
            if name == '':
                user4.insert(0, 'City')

        user4 = Entry(aut, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user4.place(x=350, y=160)
        user4.insert(0, "City")
        user4.bind('<FocusIn>', on_enter)
        user4.bind('<FocusOut>', on_leave)

        def on_enter(e):
            user5.delete(0, 'end')

        def on_leave(e):
            name = user5.get()
            if name == '':
                user3.insert(0, 'Postal Code')

        user5 = Entry(aut, width=25, fg='black', border=2,
                      bg='#add8e6', font=('Microsot YaHei Light ', 11))
        user5.place(x=70, y=200)
        user5.insert(0, "Postal Code")
        user5.bind('<FocusIn>', on_enter)
        user5.bind('<FocusOut>', on_leave)

        def Delete():
            sql = """SET FOREIGN_KEY_CHECKS=OFF"""
            cursor.execute(sql)
            sql = """Delete from auteur where nom_aut = %s"""
            cursor.execute(sql, [user2.get()])
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql2)
            selected_item1 = tree1.selection()[0]
            tree1.delete(selected_item1)
            connection.commit()

        def Exit():
            aut.destroy()

        def select():
            cursor.execute(
                """ select * from auteur where nom_aut= %s""", [user2.get()])
            a = cursor.fetchall()
            for x in a:
                user1.delete(0, END)
                user1.insert(END, x[0])
                user2.delete(0, END)
                user2.insert(END, x[1])
                user3.delete(0, END)
                user3.insert(END, x[2])
                user4.delete(0, END)
                user4.insert(END, x[3])
                user5.delete(0, END)
                user5.insert(END, x[4])
            connection.commit()

        def update():
            sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
            cursor.execute(sql1)
            sql = """ update auteur set nom_aut=%s,pre_aut=%s,ville_aut=%s,cod_post={} where id_aut={};""".format(
                user5.get(), user1.get())
            record = (user2.get(), user3.get(), user4.get())
            cursor.execute(sql, record)
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql2)
            selected_item = tree1.selection()[0]
            tree1.item(selected_item, text="blub", values=(
                user1.get(), user2.get(), user3.get(), user4.get(), user5.get()))

            connection.commit()

        def Reset():
            decision = messagebox.askquestion(
                "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
            if decision != 'yes':
                return
            else:
                sql = """SET FOREIGN_KEY_CHECKS=OFF"""
                cursor.execute(sql)
                sql1 = """DELETE FROM auteur """
                cursor.execute(sql1)
                sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
                cursor.execute(sql2)
                for item in tree1.get_children():
                    tree1.delete(item)
                connection.commit()

        def insert():
            sql = """SET FOREIGN_KEY_CHECKS=OFF"""
            cursor.execute(sql)
            mySql_insert_query = '''INSERT INTO auteur(id_aut,nom_aut,pre_aut,ville_aut,cod_post) VALUES({},%s,%s,%s,{})'''.format(
                user1.get(), user5.get())
            record = (user2.get(), user3.get(), user4.get())

            cursor.execute(mySql_insert_query, record)
            sql1 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql1)
            val = (user1.get(), user2.get(),
                   user3.get(), user4.get(), user5.get())
            tree1.insert(parent='', index=val[0],
                         iid=val[0], text='', values=val)
            connection.commit()

        btn1 = Button(aut, text="Add ",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
        btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

        btn2 = Button(aut, text=" Update", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
        btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

        btn3 = Button(aut, text="Search",
                      bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
        btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

        btn4 = Button(aut, text="Delete", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
        btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

        btn5 = Button(aut, text="Reset", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
        btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
        btn6 = Button(aut, text="Exit", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
        btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)

        tree1 = ttk.Treeview(aut, height=5)
        tree1['columns'] = ('Identifier Of Author', 'Last Name of Author',
                            'First Name of Author', 'City', 'Postal Code')
        tree1.column('#0', width=0, stretch=NO)
        tree1.column('Identifier Of Author', anchor=CENTER, width=80)
        tree1.column('Last Name of Author', anchor=CENTER, width=80)
        tree1.column('First Name of Author', anchor=CENTER, width=80)
        tree1.column('City', anchor=CENTER, width=80)
        tree1.column('Postal Code', anchor=CENTER, width=80)

        tree1.heading('#0', anchor=CENTER, text='')
        tree1.heading('Identifier Of Author', anchor=CENTER,
                      text='Identifier Of Author')
        tree1.heading('Last Name of Author', anchor=CENTER,
                      text='Last Name of Author')
        tree1.heading('First Name of Author', anchor=CENTER,
                      text='First Name of Author')
        tree1.heading('City', anchor=CENTER, text='City')
        tree1.heading('Postal Code', anchor=CENTER, text='Postal Code')
        tree1.place(x=70, y=230, relwidth=0.6, relheight=0.4)

        # query to retrieve details from books table

        connection = mysql.connector.connect(host='localhost',
                                             database='biblio',
                                             user='root',
                                             password='123654789')

        cursor = connection.cursor()
        # set variable in query
        cursor.execute('select * from auteur ')
        # fetch result
        record = cursor.fetchall()

        for i in record:
            tree1.insert(parent='', index=i[0], iid=i[0], text='', values=i)

        aut.mainloop()

    def livre_par_auteur():

        def Exit1():
            book1.destroy()
        cursor.execute(
            'select tit_doc, nom_aut,pre_aut from document e1,auteur where id_aut=(select id_aut from ecrire where code_isbn_liv=(select code_isbn_liv from livre e2 where e2.ref_doc=e1.ref_doc))')
        a = cursor.fetchall()
        book1 = Tk()
        book1.title("The national library of Rabat ")
        book1.geometry('925x500+300+200')
        book1.config(bg="#d1bea8")
        book1.resizable(False, False)
        canvas = Canvas(book1, width=925, height=500, bg="#f0f8ff")
        canvas.pack()
        btn6 = Button(book1, text="Exit", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit1)
        btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)
        t = ttk.Treeview(book1, height=5)
        t['columns'] = ('Title', 'First_Name', 'Last_name',)
        t.column('#0', width=0, stretch=NO)
        t.column('Title', anchor=CENTER, width=80)
        t.column('First_Name', anchor=CENTER, width=80)
        t.column('Last_name', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Title', anchor=CENTER, text='Title')
        t.heading('First_Name', anchor=CENTER, text='First_Name')
        t.heading('Last_name', anchor=CENTER, text='Last_name')
        t.place(x=70, y=80, relwidth=0.6, relheight=0.6)
        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        name = user1.get()
        if name == '':
            user1.insert(0, 'Reference_book')

    user1 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user1.place(x=70, y=80)
    user1.insert(0, "Reference_book")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name = user2.get()
        if name == '':
            user2.insert(0, 'Title of the book')

    user2 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user2.place(x=70, y=120)
    user2.insert(0, "Title of the book")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name = user3.get()
        if name == '':
            user3.insert(0, 'Date of publication')

    user3 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user3.place(x=350, y=80)
    user3.insert(0, "Date of publication")
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user4.delete(0, 'end')

    def on_leave(e):
        name = user4.get()
        if name == '':
            user4.insert(0, 'Name of editor')

    user4 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user4.place(x=350, y=120)
    user4.insert(0, "Name of editor")
    user4.bind('<FocusIn>', on_enter)
    user4.bind('<FocusOut>', on_leave)

    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
        sql = """Delete from document where ref_doc = {}""".format(user1.get())
        sql2 = """SET FOREIGN_KEY_CHECKS=OFF"""
        cursor.execute(sql1)
        cursor.execute(sql)
        cursor.execute(sql2)
        selected_item1 = tree.selection()[0]
        tree.delete(selected_item1)
        connection.commit()

    def Exit():
        book.destroy()

    def select():
        cursor.execute(
            """ select * from document where tit_doc=%s""", [user2.get()])
        a = cursor.fetchall()
        for x in a:
            user1.delete(0, END)
            user1.insert(END, x[0])
            user3.delete(0, END)
            user3.insert(END, x[2])
            user4.delete(0, END)
            user4.insert(END, x[3])
        connection.commit()

    def update():
        sql = """ update document set tit_doc =%s,ans_pub_doc={},edit_doc=%s where ref_doc={};""".format(
            user3.get(), user1.get())
        cursor.execute(sql, [user2.get(), user4.get()])
        selected_item = tree.selection()[0]
        tree.item(selected_item, text="blub", values=(
            user1.get(), user2.get(), user3.get(), user4.get()))
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql1 = """DELETE FROM document """
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql3)
            for item in tree.get_children():
                tree.delete(item)
            connection.commit()

    def insert():
        mySql_insert_query = '''INSERT INTO document(ref_doc,tit_doc,ans_pub_doc,edit_doc) VALUES({},%s,{},%s)'''.format(
            user1.get(), user3.get())

        record = (user2.get(), user4.get())
        cursor.execute(mySql_insert_query, record)
        val = (user1.get(), user2.get(), user3.get(), user4.get())
        tree.insert(parent='', index=val[0],
                    iid=val[0], text='', values=val)
        connection.commit()

    btn1 = Button(book, text="Add ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
    btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

    btn2 = Button(book, text=" Update", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
    btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

    btn3 = Button(book, text="Search",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
    btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

    btn4 = Button(book, text="Delete", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
    btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

    btn5 = Button(book, text="Reset", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
    btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
    btn6 = Button(book, text="Exit", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
    btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)
    btn7 = Button(book, text="Books", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=livre)
    btn7.place(x=10, y=20, relwidth=0.20, relheight=0.06)
    btn9 = Button(book, text="Newspapers and Revues", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=periodique)
    btn9.place(x=680, y=20, relwidth=0.20, relheight=0.06)
    btn8 = Button(book, text="Author", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=auteur)
    btn8.place(x=250, y=20, relwidth=0.20, relheight=0.06)
    btn10 = Button(book, text="Books and their Authors ", bg='#add8e6',
                   fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=livre_par_auteur)
    btn10.place(x=460, y=20, relwidth=0.20, relheight=0.06)
    btn11= Button(book, text="Written by who ? ", bg='#add8e6',
                   fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=ecrire)
    btn11.place(x=70, y=160, relwidth=0.20, relheight=0.06)
    tree = ttk.Treeview(book, height=5)
    tree['columns'] = ('ref_doc', 'tit_doc', 'ans_pub_doc', 'edit_doc')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ref_doc', anchor=CENTER, width=80)
    tree.column('tit_doc', anchor=CENTER, width=80)
    tree.column('ans_pub_doc', anchor=CENTER, width=80)
    tree.column('edit_doc', anchor=CENTER, width=80)

    tree.heading('#0', anchor=CENTER, text='')
    tree.heading('ref_doc', anchor=CENTER, text='ref_doc')
    tree.heading('tit_doc', anchor=CENTER, text='tit_doc')
    tree.heading('ans_pub_doc', anchor=CENTER, text='ans_pub_doc')
    tree.heading('edit_doc', anchor=CENTER, text='edit_doc')
    tree.place(x=70, y=230, relwidth=0.6, relheight=0.4)

    # query to retrieve details from books table

    connection = mysql.connector.connect(host='localhost',
                                         database='biblio',
                                         user='root',
                                         password='123654789')

    cursor = connection.cursor()
    # set variable in query
    cursor.execute('select * from document ')
    # fetch result
    record = cursor.fetchall()

    for i in record:
        tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)

    book.mainloop()

