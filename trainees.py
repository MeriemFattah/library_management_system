          
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from home import *


connection = mysql.connector.connect(host='localhost',
                                        database='biblio',
                                        user='root',
                                        password='1236547')

cursor = connection.cursor()

def trainees():
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

    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        Lname = user2.get()
        if Lname == '':
            user2.insert(0, 'Lastname')

    user2 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user2.place(x=70, y=160)
    user2.insert(0, "Lastname")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        cname = user3.get()
        if cname == '':
            user3.insert(0, 'City')

    user3 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user3.place(x=350, y=160)
    user3.insert(0, "City")
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user4.delete(0, 'end')

    def on_leave(e):
        pname = user4.get()
        if pname == '':
            user4.insert(0, 'Postal code')

    user4 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user4.place(x=350, y=80)
    user4.insert(0, "Postal code")
    user4.bind('<FocusIn>', on_enter)
    user4.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user5.delete(0, 'end')

    def on_leave(e):
        nname = user5.get()
        if nname == '':
            user5.insert(0, 'Phone number')

    user5 = Entry(mini, width=25, fg='black', border=2,
                  bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user5.place(x=350, y=120)
    user5.insert(0, "Phone number")
    user5.bind('<FocusIn>', on_enter)
    user5.bind('<FocusOut>', on_leave)

    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
        sql = """Delete from stagiaire where id_stag= {}""".format(user0.get())
        sql2 = """SET FOREIGN_KEY_CHECKS=OFF"""
        cursor.execute(sql1)
        cursor.execute(sql)
        cursor.execute(sql2)
        selected_item1 = tree.selection()[0]
        tree.delete(selected_item1)
        connection.commit()

    def Exit():
        mini.destroy()

    def select():
        cursor.execute(
            """ select * from stagiaire where id_stag={}""".format(user0.get()))
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
        connection.commit()

    def update():
        sql = """ update stagiaire set nom_stag=%s,pre_stag=%s,ville_satg=%s,code_post_stag={},num_tele_stag={} where id_stag={};""".format(
            user4.get(), user5.get(), user0.get())
        de = (user1.get(), user2.get(), user3.get())
        cursor.execute(sql, de)
        selected_item = tree.selection()[0]
        tree.item(selected_item, text="blub", values=(
            user0.get(), user1.get(), user2.get(), user3.get(), user4.get(), user5.get()))
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql1 = """DELETE FROM stagiaire """
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql3)
            for item in tree.get_children():
                tree.delete(item)
            connection.commit()

    def insert():
        mySql_insert_query = '''INSERT INTO stagiaire (id_stag,nom_stag,pre_stag,ville_satg,code_post_stag,num_tele_stag)
        VALUES({},%s,%s,%s,{},{});'''.format(user0.get(), user4.get(), user5.get())

        record = (user1.get(), user2.get(), user3.get())
        cursor.execute(mySql_insert_query, record)
        val = (user0.get(), user1.get(), user2.get(),
               user3.get(), user4.get(), user5.get())
        tree.insert(parent='', index=val[0],
                    iid=val[0], text='', values=val)
        connection.commit()


    btn1 = Button(mini, text="Add ",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
    btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

    btn2 = Button(mini, text=" Update", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
    btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

    btn3 = Button(mini, text="Search",
                  bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
    btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

    btn4 = Button(mini, text="Delete", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
    btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

    btn5 = Button(mini, text="Reset", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
    btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
    btn6 = Button(mini, text="Exit", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
    btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)
    btn7 = Button(mini, text="interns and employees ", bg='#add8e6',
                  fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=h)
    btn7.place(x=680, y=20, relwidth=0.25, relheight=0.1)

    tree = ttk.Treeview(mini, height=5)
    tree['columns'] = ('id_stag', 'nom_stag', 'pré_stag',
                       'ville_satg', 'code_post_stag', 'num_tel_stag')
    tree.column('#0', width=0, stretch=NO)
    tree.column('id_stag', anchor=CENTER, width=80)
    tree.column('nom_stag', anchor=CENTER, width=80)
    tree.column('pré_stag', anchor=CENTER, width=80)
    tree.column('ville_satg', anchor=CENTER, width=80)
    tree.column('code_post_stag', anchor=CENTER, width=80)
    tree.column('num_tel_stag', anchor=CENTER, width=80)

    tree.heading('#0', anchor=CENTER, text='')
    tree.heading('id_stag', anchor=CENTER, text='id_stag')
    tree.heading('nom_stag', anchor=CENTER, text='nom_stag')
    tree.heading('pré_stag', anchor=CENTER, text='pré_stag')
    tree.heading('ville_satg', anchor=CENTER, text='ville_satg')
    tree.heading('code_post_stag', anchor=CENTER, text='code_post_stag')
    tree.heading('num_tel_stag', anchor=CENTER, text='num_tel_stag')
    tree.place(x=70, y=230, relwidth=0.6, relheight=0.4)

    # query to retrieve details from books table

    connection = mysql.connector.connect(host='localhost',
                                         database='biblio',
                                         user='root',
                                         password='1236547')

    cursor = connection.cursor()
    # set variable in query
    cursor.execute('select * from  stagiaire')
    # fetch result
    record = cursor.fetchall()

    for i in record:
        tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)

    mini.mainloop()


