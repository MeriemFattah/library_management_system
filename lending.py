from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox


connection = mysql.connector.connect(host='localhost',
                                        database='biblio',
                                        user='root',
                                        password='1236547')

cursor = connection.cursor()

def lending():
    book = Tk()
    book.title("The national library of Rabat ")
    book.geometry('925x500+300+200')
    book.config(bg="#d1bea8")
    book.resizable(False, False)
    canvas = Canvas(book, width=925, height=500, bg="#f0f8ff")
    canvas.pack()

    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        name = user1.get()
        if name == '':
            user1.insert(0, 'Number of lending')

    user1 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user1.place(x=70, y=80)
    user1.insert(0, "Number of lending")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name = user2.get()
        if name == '':
            user2.insert(0, 'Beginning Date')

    user2 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user2.place(x=70, y=120)
    user2.insert(0, "Beginning Date")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name = user3.get()
        if name == '':
            user3.insert(0, ' Due Date')

    user3 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user3.place(x=350, y=80)
    user3.insert(0, "Due Date")
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user4.delete(0, 'end')

    def on_leave(e):
        name = user4.get()
        if name == '':
            user4.insert(0, 'Id Borrower')

    user4 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user4.place(x=350, y=120)
    user4.insert(0, "Id of Borrower")
    user4.bind('<FocusIn>', on_enter)
    user4.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user5.delete(0, 'end')

    def on_leave(e):
        name = user5.get()
        if name == '':
            user5.insert(0, 'Id of Employee')

    user5 = Entry(book, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user5.place(x=70, y=160)
    user5.insert(0, "Id of Employee")
    user5.bind('<FocusIn>', on_enter)
    user5.bind('<FocusOut>', on_leave)

    def samples():

        book2 = Tk()
        book2.title("The national library of Rabat ")
        book2.geometry('925x500+300+200')
        book2.config(bg="#d1bea8")
        book2.resizable(False, False)
        canvas = Canvas(book2, width=925, height=500, bg="#f0f8ff")
        canvas.pack()

        def on_enter(e):
            u1.delete(0, 'end')

        def on_leave(e):
            name = u1.get()
            if name == '':
                u1.insert(0, 'Number')

        u1 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u1.place(x=70, y=80)
        u1.insert(0, "Number")
        u1.bind('<FocusIn>', on_enter)
        u1.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u2.delete(0, 'end')

        def on_leave(e):
            name = u2.get()
            if name == '':
                u2.insert(0, 'Date_buying')

        u2 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u2.place(x=70, y=120)
        u2.insert(0, "Date_buying")
        u2.bind('<FocusIn>', on_enter)
        u2.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u3.delete(0, 'end')

        def on_leave(e):
            name = u3.get()
            if name == '':
                u3.insert(0, 'Fee')

        u3 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u3.place(x=70, y=160)
        u3.insert(0, "Fee")
        u3.bind('<FocusIn>', on_enter)
        u3.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u4.delete(0, 'end')

        def on_leave(e):
            name = u4.get()
            if name == '':
                u4.insert(0, 'Reference_doc')

        u4 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u4.place(x=350, y=80)
        u4.insert(0, "Reference_doc")
        u4.bind('<FocusIn>', on_enter)
        u4.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u5.delete(0, 'end')

        def on_leave(e):
            name = u5.get()
            if name == '':
                u5.insert(0, 'Avaibility')

        u5 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u5.place(x=350, y=120)
        u5.insert(0, "Avaibility")
        u5.bind('<FocusIn>', on_enter)
        u5.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u6.delete(0, 'end')

        def on_leave(e):
            name = u6.get()
            if name == '':
                u6.insert(0, 'Statement')

        u6 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u6.place(x=350, y=160)
        u6.insert(0, "Statement")
        u6.bind('<FocusIn>', on_enter)
        u6.bind('<FocusOut>', on_leave)

        def on_enter(e):
            u7.delete(0, 'end')

        def on_leave(e):
            name = u7.get()
            if name == '':
                u7.insert(0, 'Id_user')

        u7 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u7.place(x=70, y=200)
        u7.insert(0, "Id_user")
        u7.bind('<FocusIn>', on_enter)
        u7.bind('<FocusOut>', on_leave)


        def on_enter(e):
            u8.delete(0, 'end')

        def on_leave(e):
            name = u8.get()
            if name == '':
                u8.insert(0, 'Number of samples')

        u8 = Entry(book2, width=25, fg='black', border=2,
                   bg='#add8e6', font=('Microsot YaHei Light ', 11))
        u8.place(x=350, y=200)
        u8.insert(0, "Number of samples")
        u8.bind('<FocusIn>', on_enter)
        u8.bind('<FocusOut>', on_leave)

        def insert():

            sql = """SET FOREIGN_KEY_CHECKS=0 """
            cursor.execute(sql)
            mySql_insert_query = '''INSERT INTO exemplaire (n°exemp,dat_achat_exemp,Nbr_exemp,id_util,amende_forfait,ref_doc,type_exemp,etat_exemp) VALUES({},%s,{},{},{},{},%s,%s)'''.format(
                u1.get(),u8.get(), u7.get(), u3.get(), u4.get())

            cursor.execute(mySql_insert_query, [u2.get(),u5.get(), u6.get()])
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql3)
            val = (u1.get(), u2.get(),u8.get(), u7.get(),
                   u3.get(), u4.get(), u5.get(), u6.get())
            t.insert(parent='', index=val[0],
                     iid=val[0], text='', values=val)
            connection.commit()

        def Delete():
            sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
            sql = """Delete from exemplaire where n°exemp = {}""".format(
                u1.get())
            sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
            cursor.execute(sql1)
            cursor.execute(sql)
            cursor.execute(sql2)
            selected_item1 = t.selection()[0]
            t.delete(selected_item1)
            connection.commit()

        def select():
            cursor.execute(
                """ select * from exemplaire where n°exemp={}""".format(u1.get()))
            a = cursor.fetchall()
            for x in a:
                u2.delete(0, END)
                u2.insert(END, x[1])
                u3.delete(0, END)
                u3.insert(END, x[2])
                u4.delete(0, END)
                u4.insert(END, x[4])
                u5.delete(0, END)
                u5.insert(END, x[5])
                u6.delete(0, END)
                u6.insert(END, x[6])
                u7.delete(0, END)
                u7.insert(END, x[3])
            connection.commit()

        def Exit1():
            book2.destroy()

        cursor.execute('select * from exemplaire')
        a = cursor.fetchall()

        btn6 = Button(book2, text="Add", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
        btn6.place(x=680, y=80, relwidth=0.25, relheight=0.1)

        btn7 = Button(book2, text="Exit", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit1)
        btn7.place(x=680, y=260, relwidth=0.25, relheight=0.1)
        btn8 = Button(book2, text="Select", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
        btn8.place(x=680, y=140, relwidth=0.25, relheight=0.1)
        btn9 = Button(book2, text="Delete", bg='#add8e6',
                      fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Delete)
        btn9.place(x=680, y=200, relwidth=0.25, relheight=0.1)
        t = ttk.Treeview(book2, height=5)
        t['columns'] = ('Number', 'Date_buying','Number_samples' ,'Id_user', 'Fee',
                        'Reference_doc', 'Avaibility', 'Statement')
        t.column('#0', width=0, stretch=NO)
        t.column('Number', anchor=CENTER, width=80)
        t.column('Date_buying', anchor=CENTER, width=80)
        t.column('Number_samples', anchor=CENTER, width=80)
        t.column('Id_user', anchor=CENTER, width=80)
        t.column('Fee', anchor=CENTER, width=80)
        t.column('Reference_doc', anchor=CENTER, width=80)
        t.column('Avaibility', anchor=CENTER, width=80)
        t.column('Statement', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Number', anchor=CENTER, text='Number')
        t.heading('Date_buying', anchor=CENTER, text='Date_buying')
        t.heading('Number_samples', anchor=CENTER, text='Number_samples')
        t.heading('Id_user', anchor=CENTER, text='Id_user')
        t.heading('Fee', anchor=CENTER, text='Fee')
        t.heading('Reference_doc', anchor=CENTER, text='Reference_doc')
        t.heading('Avaibility', anchor=CENTER, text='Avaibility')
        t.heading('Statement', anchor=CENTER, text='Statement')
        t.place(x=70, y=240, relwidth=0.6, relheight=0.4)
        for i in a:
            t.insert('', 'end', values=i)
        book2.mainloop()

    def Sample():

        def Exit1():
            book1.destroy()
        cursor.execute(
            ' select id_util , count(id_emp) as nombre_emprunt from emprunt group by (id_util);')
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
        t['columns'] = ('Id_User', 'Number_book')
        t.column('#0', width=0, stretch=NO)
        t.column('Id_User', anchor=CENTER, width=80)
        t.column('Number_book', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Id_User', anchor=CENTER, text='Id_User')
        t.heading('Number_book', anchor=CENTER, text='Number_book')
        t.place(x=70, y=80, relwidth=0.6, relheight=0.6)
        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def avaibility():

        def Exit1():
            book1.destroy()
        cursor.execute(
            'select type_exemp ,tit_doc from exemplaire e1,document e2 where ( e1.ref_doc=e2.ref_doc )')
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
        t['columns'] = ('Avaibility', 'Title')
        t.column('#0', width=0, stretch=NO)
        t.column('Avaibility', anchor=CENTER, width=80)
        t.column('Title', anchor=CENTER, width=80)

        t.heading('#0', anchor=CENTER, text='')
        t.heading('Avaibility', anchor=CENTER, text='Avaibility')
        t.heading('Title', anchor=CENTER, text='Title')
        t.place(x=70, y=80, relwidth=0.6, relheight=0.6)
        for i in a:
            t.insert('', 'end', values=i)
        book1.mainloop()

    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
        sql = """Delete from emprunt where id_emp = {}""".format(user1.get())
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
            """ select * from emprunt where id_emp={}""".format(user1.get()))
        a = cursor.fetchall()
        for x in a:
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
        sql = """SET FOREIGN_KEY_CHECKS=OFF"""
        cursor.execute(sql)
        sql1 = """ UPDATE emprunt set dat_deb_emp =%s,dat_fin_emp=%s,id_util={} ,id_biblio={} where id_emp={}  """.format(
            user4.get(), user5.get(), user1.get())
        cursor.execute(sql1, [user2.get(), user3.get()])
        sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
        cursor.execute(sql2)
        selected_item = tree.selection()[0]
        tree.item(selected_item, text="blub", values=(
            user1.get(), user2.get(), user3.get(), user4.get(), user5.get()))
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql1 = """DELETE FROM emprunt """
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql3)
            for item in tree.get_children():
                tree.delete(item)
            connection.commit()

    def insert():

        sql = """SET FOREIGN_KEY_CHECKS=0 """
        cursor.execute(sql)
        mySql_insert_query = '''INSERT INTO emprunt(id_emp,dat_deb_emp,dat_fin_emp,id_util,id_biblio) VALUES({},%s,%s,{},{})'''.format(
            user1.get(), user4.get(), user5.get())

        cursor.execute(mySql_insert_query, [user2.get(), user3.get()])
        sql3 = """SET FOREIGN_KEY_CHECKS=1"""
        cursor.execute(sql3)
        val = (user1.get(), user2.get(), user3.get(), user4.get(), user5.get())
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
    btn7 = Button(book, text="Books Avaibility ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=avaibility)
    btn7.place(x=680, y=20, relwidth=0.25, relheight=0.1)
    btn7 = Button(book, text="Samples ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=samples)
    btn7.place(x=350, y=160, relwidth=0.22, relheight=0.1)
    btn8 = Button(book, text="Users and books ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Sample)
    btn8.place(x=350, y=10, relwidth=0.22, relheight=0.1)

    tree = ttk.Treeview(book, height=5)
    tree['columns'] = ('Number', 'Date_B', 'Date_E', 'User', 'Employee')
    tree.column('#0', width=0, stretch=NO)
    tree.column('Number', anchor=CENTER, width=80)
    tree.column('Date_B', anchor=CENTER, width=80)
    tree.column('Date_E', anchor=CENTER, width=80)
    tree.column('User', anchor=CENTER, width=80)
    tree.column('Employee', anchor=CENTER, width=80)

    tree.heading('#0', anchor=CENTER, text='')
    tree.heading('Number', anchor=CENTER, text='Number')
    tree.heading('Date_B', anchor=CENTER, text='Date_B')
    tree.heading('Date_E', anchor=CENTER, text='Date_E')
    tree.heading('User', anchor=CENTER, text='User')
    tree.heading('Employee', anchor=CENTER, text='Employee')
    tree.place(x=70, y=230, relwidth=0.6, relheight=0.4)

    # query to retrieve details from books table

    connection = mysql.connector.connect(host='localhost',
                                         database='biblio',
                                         user='root',
                                         password='123654789')

    cursor = connection.cursor()
    # set variable in query
    cursor.execute('select * from emprunt ')
    # fetch result
    record = cursor.fetchall()

    for i in record:
        tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)

    book.mainloop()