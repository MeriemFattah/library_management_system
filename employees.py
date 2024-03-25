
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

def employees():
    emp = Tk()
    emp.title('The national library of Rabat')
    emp.geometry('925x500+300+200')
    emp.config(bg="white")
    # ne permet pas le redimensionnement de la fenetre.
    emp.resizable(False, False)
    canvas = Canvas(emp, width=925, height=500, bg="#f0f8ff")
    canvas.pack()

    def on_enter(e):
        user0.delete(0, 'end')

    def on_leave(e):
        fname = user0.get()
        if fname == '':
            user0.insert(0, 'CIN')

    user0 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user0.place(x=70, y=80)
    user0.insert(0, "CIN")
    user0.bind('<FocusIn>', on_enter)
    user0.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user00.delete(0, 'end')

    def on_leave(e):
        fname = user00.get()
        if fname == '':
            user00.insert(0, 'Firstname')

    user00 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user00.place(x=70, y=120)
    user00.insert(0, "First Name")
    user00.bind('<FocusIn>', on_enter)
    user00.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        fname = user1.get()
        if fname == '':
            user1.insert(0, 'Lastname')

    user1 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user1.place(x=70, y=160)
    user1.insert(0, "Lastname")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        Lname = user2.get()
        if Lname == '':
            user2.insert(0, 'Date of birth')

    user2 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user2.place(x=350, y=80)
    user2.insert(0, "Date of birth")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        cname = user3.get()
        if cname == '':
            user3.insert(0, 'City')

    user3 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user3.place(x=70, y=240)
    user3.insert(0, "City")
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user4.delete(0, 'end')

    def on_leave(e):
        pname = user4.get()
        if pname == '':
            user4.insert(0, 'Postal code')

    user4 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user4.place(x=350, y=160)
    user4.insert(0, "Postal code")
    user4.bind('<FocusIn>', on_enter)
    user4.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user5.delete(0, 'end')

    def on_leave(e):
        nname = user5.get()
        if nname == '':
            user5.insert(0, 'Position')

    user5 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user5.place(x=70, y=200)
    user5.insert(0, "Position")
    user5.bind('<FocusIn>', on_enter)
    user5.bind('<FocusOut>', on_leave)


    def on_enter(e):
        user6.delete(0, 'end')

    def on_leave(e):
        fname = user6.get()
        if fname == '':
            user6.insert(0, 'Phone number')
    user6 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user6.place(x=350, y=200)
    user6.insert(0, " Phone number")
    user6.bind('<FocusIn>', on_enter)
    user6.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user7.delete(0, 'end')

    def on_leave(e):
        nname = user7.get()
        if nname == '':
            user7.insert(0, ' Name of category')

    user7 = Entry(emp, width=25, fg='black', border=2,
                    bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user7.place(x=350, y=120)
    user7.insert(0, " Name of category")
    user7.bind('<FocusIn>', on_enter)
    user7.bind('<FocusOut>', on_leave)

    def update():
        sql = """SET FOREIGN_KEY_CHECKS=OFF"""
        cursor.execute(sql)
        sql1 = """ update bibliothecaire set nom_biblio =%s ,pre_biblio  =%s,date_n_biblio =%s ,ville_biblio =%s,code_post_biblio ={},pos_biblio =%s,
        num_tele_biblio={},nom_categbiblio=%s where id_biblio={}""".format(user4.get(), user6.get(), user0.get())
        cursor.execute(sql1, [user00.get(), user1.get(), user2.get(),
                        user3.get(), user5.get(),user7.get()])
        sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
        cursor.execute(sql2)
        selected_item = tree.selection()[0]
        tree.item(selected_item, text="blub", values=(user0.get(), user00.get(), user1.get(
        ), user2.get(), user3.get(), user4.get(), user5.get(), user6.get(), user7.get()))
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql1 = """DELETE FROM bibliothecaire """
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql3)
            for item in tree.get_children():
                tree.delete(item)
            connection.commit()

    def select():
        cursor.execute(
            """ select * from bibliothecaire where id_biblio={}""".format(user0.get()))
        a = cursor.fetchall()
        for x in a:
            user00.delete(0, END)
            user00.insert(END, x[1])
            user1.delete(0, END)
            user1.insert(END, x[2])
            user2.delete(0, END)
            user2.insert(END, x[3])
            user3.delete(0, END)
            user3.insert(END, x[4])
            user4.delete(0, END)
            user4.insert(END, x[5])
            user5.delete(0, END)
            user5.insert(END, x[6])
            user6.delete(0, END)
            user6.insert(END, x[7])
            user7.delete(0, END)
            user7.insert(END, x[8])
        connection.commit()

    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
        sql = """Delete from bibliothecaire where id_biblio = {}""".format(
            user0.get())
        sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
        cursor.execute(sql1)
        cursor.execute(sql)
        cursor.execute(sql2)
        selected_item1 = tree.selection()[0]
        tree.delete(selected_item1)
        connection.commit()

    def exit():
        emp.destroy()

    def insert():
        sql = """SET FOREIGN_KEY_CHECKS=0;"""
        cursor.execute(sql)
        mySql_insert_query = '''INSERT INTO bibliothecaire (id_biblio,nom_biblio ,pre_biblio ,date_n_biblio ,ville_biblio,code_post_biblio ,pos_biblio,num_tele_biblio,nom_categbiblio )
        VALUES({},%s,%s,%s,%s,{},%s,{},%s)'''.format(
            user0.get(), user4.get(), user6.get())

        record = (user00.get(), user1.get(), user2.get(),
                    user3.get(), user5.get(), user7.get())
        cursor.execute(mySql_insert_query, record)
        sql1 = """SET FOREIGN_KEY_CHECKS=1;"""
        cursor.execute(sql1)
        val = (user0.get(), user00.get(), user1.get(), user2.get(), user3.get(), user4.get(),
                user5.get(), user6.get(), user7.get())
        tree.insert(parent='', index=val[0],
                    iid=val[0], text='', values=val)
        connection.commit()

    btn1 = Button(emp, text="Add",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
    btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)
    btn2 = Button(emp, text="Update",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
    btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)
    btn3 = Button(emp, text="Search",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
    btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)
    btn4 = Button(emp, text="Delete",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Delete)
    btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)
    btn5 = Button(emp, text="Reset",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
    btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
    btn6 = Button(emp, text="Exit",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=exit)
    btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)

    tree = ttk.Treeview(emp, columns=(
        1, 2, 3, 4, 5, 6, 7, 8, 9), heigh=10, show='headings')
    tree.place(x=50, y=280, width=550, height=220)
    tree.heading(1, text='id')
    tree.heading(2, text='F_Name')
    tree.heading(3, text='L_Name')
    tree.heading(4, text='D_birth')
    tree.heading(5, text='City')
    tree.heading(6, text='P_code')
    tree.heading(7, text='position')
    tree.heading(9, text='category')
    tree.heading(8, text='Ph_number')
    tree.column(1, width=50)
    tree.column(2, width=50)
    tree.column(3, width=50)
    tree.column(4, width=50)
    tree.column(5, width=50)
    tree.column(6, width=50)
    tree.column(7, width=50)
    tree.column(8, width=50)
    tree.column(9, width=50)
    connection = mysql.connector.connect(host='localhost',
                                            database='biblio',
                                            user='root',
                                            password='1236547')

    sql_select_Query = "select * from bibliothecaire"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        tree.insert('', END, values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    emp.mainloop()
