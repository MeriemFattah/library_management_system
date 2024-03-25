
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


def members():
    def Exit():
        mini.destroy()

    def select():
        cursor.execute(
            """ select * from utilisateur where id_util={}""".format(user0.get()))
        a = cursor.fetchall()
        for x in a:
            user0.delete(0, END)
            user0.insert(END, x[0])
            user1.delete(0, END)
            user1.insert(END, x[1])
            user2.delete(0, END)
            user2.insert(END, x[2])
            user3.delete(0, END)
            user3.insert(END, x[3])
            user4.delete(0, END)
            user4.insert(END, x[4])
            user5.delete(0, END)
            user5.insert(END, x[5])
            user6.delete(0, END)
            user6.insert(END, x[6])
            user8.delete(0, END)
            user8.insert(END, x[7])
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql4 = """DELETE FROM utilisateur"""
            sql1 = """SET FOREIGN_KEY_CHECKS=1 """
            cursor.execute(sql)
            cursor.execute(sql4)
            cursor.execute(sql1)
            sql2 = """SET FOREIGN_KEY_CHECKS=0 """
            sql3 = """DELETE FROM emprunt"""
            sql5 = """SET FOREIGN_KEY_CHECKS=1 """
            cursor.execute(sql2)
            cursor.execute(sql3)
            cursor.execute(sql5)
            for item in tree.get_children():
                tree.delete(item)
            connection.commit()

    def update():
        sql1 = """SET FOREIGN_KEY_CHECKS=0;"""
        sql = """update utilisateur set nom_util=%s,pre_util=%s,date_n_util=%s,ville_util=%s,code_post_util={},num_tel_util={},type_util=%s where id_util={};""".format(
            user5.get(), user6.get(), user0.get())
        rep = (user1.get(), user2.get(), user3.get(), user4.get(), user8.get())
        sql2 = """SET FOREIGN_KEY_CHECKS=1;"""
        cursor.execute(sql1)
        cursor.execute(sql, rep)
        cursor.execute(sql2)
        selected_item = tree.selection()[0]
        tree.item(selected_item, text="blub", values=(user0.get(), user1.get(
        ), user2.get(), user3.get(), user4.get(), user5.get(), user6.get(), user8.get()))
        connection.commit()

    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=0;"""
        cursor.execute(sql1)
        sql = """Delete from utilisateur where id_util = {}""".format(
            user0.get())
        cursor.execute(sql)
        sql2 = """SET FOREIGN_KEY_CHECKS=1;"""
        cursor.execute(sql2)
        selected_item1 = tree.selection()[0]
        tree.delete(selected_item1)
        connection.commit()

    def insert():
        mySql_insert_query = '''INSERT INTO utilisateur (id_util,nom_util ,pre_util ,date_n_util ,ville_util,code_post_util,num_tel_util,type_util)
                VALUES({},%s,%s,%s,%s,{},{},%s)'''.format(
            user0.get(), user5.get(), user6.get())
        record = (user1.get(), user2.get(),
                  user3.get(), user4.get(), user8.get())
        cursor.execute(mySql_insert_query, record)
        val = (user0.get(),  user1.get(), user2.get(), user3.get(), user4.get(),
               user5.get(), user6.get(), user8.get())
        tree.insert(parent='', index=val[0],
                    iid=val[0], text='', values=val)
        connection.commit()

    mini = Tk()
    mini.title("The national library of Rabat ")
    mini.geometry('925x500+300+200')
    mini.config(bg="white")
    mini.resizable(False, False)

    canvas = Canvas(mini, width=925, height=500, bg="#f0f8ff")
    canvas.pack()

    def on_enter(e):
        user0.delete(0, 'end')

    def on_leave(e):
        fname = user0.get()
        if fname == '':
            user0.insert(0, 'CIN')

    user0 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user0.place(x=70, y=80)
    user0.insert(0, "CIN")
    user0.bind('<FocusIn>', on_enter)
    user0.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        fname = user1.get()
        if fname == '':
            user1.insert(0, 'Firstname')

    user1 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user1.place(x=70, y=120)
    user1.insert(0, "Firstname")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)
    user2 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))

    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        Lname = user2.get()
        if Lname == '':
            user2.insert(0, 'Lastname')

    user2.place(x=70, y=160)
    user2.insert(0, "Lastname")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        cname = user3.get()
        if cname == '':
            user3.insert(0, 'date of birth')

    user3 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user3.place(x=70, y=200)
    user3.insert(0, "date of birth")
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user4.delete(0, 'end')

    def on_leave(e):
        pname = user4.get()
        if pname == '':
            user4.insert(0, 'city')

    user4 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user4.place(x=350, y=80)
    user4.insert(0, "city")
    user4.bind('<FocusIn>', on_enter)
    user4.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user5.delete(0, 'end')

    def on_leave(e):
        nname = user5.get()
        if nname == '':
            user5.insert(0, 'postal code')

    user5 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user5.place(x=350, y=120)
    user5.insert(0, "postal code ")
    user5.bind('<FocusIn>', on_enter)
    user5.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user6.delete(0, 'end')

    def on_leave(e):
        dname = user6.get()
        if dname == '':
            user6.insert(0, 'Phone Number')

    user6 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user6.place(x=350, y=160)
    user6.insert(0, "Phone Number")
    user6.bind('<FocusIn>', on_enter)
    user6.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user8.delete(0, 'end')

    def on_leave(e):
        dname = user8.get()
        if dname == '':
            user8.insert(0, 'type ')

    user8 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user8.place(x=350, y=200)
    user8.insert(0, "type")
    user8.bind('<FocusIn>', on_enter)
    user8.bind('<FocusOut>', on_leave)

    btn1 = Button(mini, text=" Add ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
    btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

    btn2 = Button(mini, text=" Update", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
    btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

    btn3 = Button(mini, text="Search",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
    btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

    btn4 = Button(mini, text="Delete", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Delete)
    btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

    btn5 = Button(mini, text="Reset", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
    btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
    btn6 = Button(mini, text="Exit", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
    btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)
    tree = ttk.Treeview(mini, columns=(1, 2, 3, 4, 5, 6, 7, 8),
                        heigh=5, show='headings')
    tree.place(x=70, y=240, relwidth=0.6, relheight=0.4)
    tree.heading(1, text="Id")
    tree.heading(2, text="F_name")
    tree.heading(3, text="L_name")
    tree.heading(4, text="D_birth")
    tree.heading(5, text="City")
    tree.heading(6, text="P_code")
    tree.heading(8, text='type')
    tree.heading(7, text="Ph_number")

    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    tree.column(4, width=100)
    tree.column(5, width=100)
    tree.column(6, width=100)
    tree.column(7, width=100)
    tree.column(8, width=100)

    y = 0.25  # declare var to increase the height at y-axis to print details
    # query to retrieve details from books table

    connection = mysql.connector.connect(host='localhost',
                                         database='biblio',
                                         user='root',
                                         password='123654789')

    cursor = connection.cursor()
    # set variable in query
    cursor.execute('select *from utilisateur')
    # fetch result
    record = cursor.fetchall()

    for i in record:
        tree.insert('', END, values=(
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

    mini.mainloop()
