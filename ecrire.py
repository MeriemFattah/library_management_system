
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

connection = mysql.connector.connect(
    host='localhost', database='biblio', user='root', password='1236547')
cursor = connection.cursor()
def ecrire ():
    m = Tk()
    m.title("The national library of Rabat ")
    m.geometry('925x500+300+200')
    m.config(bg="white")
    m.resizable(False, False)
    canvas = Canvas(m, width=925, height=500, bg="#f0f8ff")
    canvas.pack()
    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        fname = user1.get()
        if fname == '':
            user1.insert(0, 'Id_book')

    user1 = Entry(m, width=25, fg='black', border=2,
                bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user1.place(x=70, y=120)
    user1.insert(0, "Id_book")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)
    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        fname = user2.get()
        if fname == '':
            user2.insert(0, 'Id_author')

    user2 = Entry(m, width=25, fg='black', border=2,
                bg='#add8e6', font=('Microsot YaHei Light ', 11))
    user2.place(x=350, y=120)
    user2.insert(0, "Id_author")
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    def insert():
        sql1 = """SET FOREIGN_KEY_CHECKS=0 """
        sql3 = """SET FOREIGN_KEY_CHECKS=1"""
        mySql_insert_query = '''INSERT INTO ecrire (code_isbn_liv,id_aut)
        VALUES({},{});'''.format(user1.get(), user2.get())
        cursor.execute(sql1)
        cursor.execute(mySql_insert_query)
        cursor.execute(sql3)
        val = ( user1.get(), user2.get())
        tre.insert(parent='', index=val[0],
                    iid=val[0], text='', values=val)
        connection.commit()
    def Delete():
        sql1 = """SET FOREIGN_KEY_CHECKS=OFF"""
        sql = """Delete from ecrire where code_isbn_liv= {}""".format(user1.get())
        sql2 = """SET FOREIGN_KEY_CHECKS=ON"""
        cursor.execute(sql1)
        cursor.execute(sql)
        cursor.execute(sql2)
        selected_item1 = tre.selection()[0]
        tre.delete(selected_item1)
        connection.commit()

    def Exit():
        m.destroy()

    def select():
        cursor.execute(
            """ select * from ecrire where code_isbn_liv={}""".format(user1.get()))
        a = cursor.fetchall()
        for x in a:
            user1.delete(0, END)
            user1.insert(END, x[0])
            user2.delete(0, END)
            user2.insert(END, x[1])
        connection.commit()

    def update():
        sql1 = """SET FOREIGN_KEY_CHECKS=0 """
        sql3 = """SET FOREIGN_KEY_CHECKS=1"""
        cursor.execute(sql1)
        sql = """ update ecrire set code_isbn_liv={} where id_aut={};""".format(user1.get(),user2.get())
        cursor.execute(sql)
        sql3 = """SET FOREIGN_KEY_CHECKS=1"""
        cursor.execute(sql3)
        selected_item = tre.selection()[0]
        tre.item(selected_item, text="blub", values=( user1.get(), user2.get()))
        connection.commit()

    def Reset():
        decision = messagebox.askquestion(
            "warning !", "DO YOU REALLY WANT TO DELETE ALL THE DATA ?")
        if decision != 'yes':
            return
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0 """
            sql1 = """DELETE FROM ecrire """
            sql3 = """SET FOREIGN_KEY_CHECKS=1"""
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql3)
            for item in tre.get_children():
                tre.delete(item)
            connection.commit()





    btn1 = Button(m, text="Add ",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=insert)
    btn1.place(x=680, y=80, relwidth=0.25, relheight=0.1)

    btn2 = Button(m, text=" Update", bg='#add8e6',
                    fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=update)
    btn2.place(x=680, y=140, relwidth=0.25, relheight=0.1)

    btn3 = Button(m, text="Search",
                    bg='#add8e6', fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=select)
    btn3.place(x=680, y=200, relwidth=0.25, relheight=0.1)

    btn4 = Button(m, text="Delete", bg='#add8e6',
                    fg="black", font=('microsft YaHei Light ',     11, 'bold'), command=Delete)
    btn4.place(x=680, y=260, relwidth=0.25, relheight=0.1)

    btn5 = Button(m, text="Reset", bg='#add8e6',
                    fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Reset)
    btn5.place(x=680, y=320, relwidth=0.25, relheight=0.1)
    btn6 = Button(m, text="Exit", bg='#add8e6',
                    fg="black", font=('microsft YaHei Light ', 11, 'bold'), command=Exit)
    btn6.place(x=680, y=380, relwidth=0.25, relheight=0.1)
    tre = ttk.Treeview(m, height=5)
    tre['columns'] = ('id_book', 'id_author')
    tre.column('#0', width=0, stretch=NO)
    tre.column('id_book', anchor=CENTER, width=80)
    tre.column('id_author', anchor=CENTER, width=80)

    tre.heading('#0', anchor=CENTER, text='')
    tre.heading('id_book', anchor=CENTER, text='id_book')
    tre.heading('id_author', anchor=CENTER, text='id_author')
    tre.place(x=70, y=230, relwidth=0.6, relheight=0.4)
    cursor.execute('select * from  ecrire')
    # fetch result
    record = cursor.fetchall()
    for i in record:
        tre.insert(parent='', index=i[0], iid=i[0], text='', values=i)


    m.mainloop()




