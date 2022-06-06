from tkinter import *
import sqlite3

def submit():
    conn = sqlite3.connect('note_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO person VALUES (:id, :pre_id, :name, :date_of_birth, :gender, :address)",
        {
            'id': id.get(),
            'pre_id': pre_id.get(),
            'name': name.get(),
            'date_of_birth': date_of_birth.get(),
            'gender': gender.get(),
            'address': address.get()
        })
    conn.commit()
    conn.close()
    # -------------------------------
    id.delete(0, END)
    pre_id.delete(0, END)
    name.delete(0, END)
    date_of_birth.delete(0, END)
    gender.delete(0, END)
    address.delete(0, END)

def show():
    conn = sqlite3.connect('note_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM person")
    records = c.fetchall()
    inc = 0
    for record in records:
        context = f'{record[0]} - {record[1]} - {record[2]} - {record[3]} - {record[4]} - {record[5]}'
        show_label = Label(root, text=context)
        show_label.grid(row=8+inc, column=0, columnspan=2)
        inc += 1
    conn.commit()
    conn.close()


root = Tk()
root.title('Note book')
root.geometry('400x400')

# conn = sqlite3.connect('note_book.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE person (
#             id integer,
#             pre_id integer,
#             name text,
#             date_of_birth text,
#             gender text,
#             address text
#         )""")
# conn.commit()
# conn.close()

id_label = Label(root, text='ID:')
id_label.grid(row=0, column=0, sticky='w')
id = Entry(root, width=40)
id.grid(row=0, column=1)

pre_id_label = Label(root, text='Pre-ID:')
pre_id_label.grid(row=1, column=0, sticky='w')
pre_id = Entry(root, width=40)
pre_id.grid(row=1, column=1)

name_label = Label(root, text='Full Name:')
name_label.grid(row=2, column=0, sticky='w')
name = Entry(root, width=40)
name.grid(row=2, column=1)

date_of_birth_label = Label(root, text='Date of birth:')
date_of_birth_label.grid(row=3, column=0, sticky='w')
date_of_birth = Entry(root, width=40)
date_of_birth.grid(row=3, column=1)

gender_label = Label(root, text='Gender:')
gender_label.grid(row=4, column=0, sticky='w')
gender = Entry(root, width=40)
gender.grid(row=4, column=1)

address_label = Label(root, text='Address:')
address_label.grid(row=5, column=0, sticky='w')
address = Entry(root, width=40)
address.grid(row=5, column=1)

submit_btn = Button(root, text='Add to database', command=submit)
submit_btn.grid(row=6, column=0, pady=(10,0), sticky='w')

show_btn = Button(root, text='Show records', command=show)
show_btn.grid(row=6, column=1, pady=(10,0), ipadx=8, sticky='w')

root.mainloop()
