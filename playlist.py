from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        #print(selected_tuple)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        e1.delete(0, END)
        e1.insert(END, 'Try view all button first')


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(song_txt.get(), singer_txt.get(), album_txt.get(), year_txt.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(song_txt.get(), singer_txt.get(), album_txt.get(), year_txt.get())
    list1.delete(0, END)
    list1.insert(END, (song_txt.get(), singer_txt.get(), album_txt.get(), year_txt.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def update_command():
    backend.update(selected_tuple[0], song_txt.get(), singer_txt.get(), album_txt.get(), year_txt.get())
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

window = Tk()

window.wm_title('Favolite songs! my playlist')

l1 = Label(window, text='Song: ')
l1.grid(row=0, column=0)

l2 = Label(window, text='Singer: ')
l2.grid(row=1, column=0)

l3 = Label(window, text='Album: ')
l3.grid(row=0, column=2)

l4 = Label(window, text='Year: ')
l4.grid(row=1, column=2)

song_txt = StringVar()
e1 = Entry(window, width=26, textvariable=song_txt)
e1.grid(row=0, column=1)

singer_txt = StringVar()
e2 = Entry(window, width=26, textvariable=singer_txt)
e2.grid(row=1, column=1)

album_txt = StringVar()
e3 = Entry(window, width=26, textvariable=album_txt)
e3.grid(row=0, column=3)

year_txt = StringVar()
e4 = Entry(window, width=26, textvariable=year_txt)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=34, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan= 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Add song', width=12, command=add_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Search one', width=12, command=search_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update selected', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete selected', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()