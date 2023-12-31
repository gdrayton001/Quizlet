from Set import Set
from tkinter import *
from tkinter import ttk
import os

def on_mousewheel(event):
    my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root=Tk()
root.title("Quizlet")
root.geometry("500x400")
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
x_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
x_scrollbar.pack(side=BOTTOM, fill=X)
my_canvas.configure(xscrollcommand=x_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
my_canvas.bind('<MouseWheel>', on_mousewheel)
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

def add_flashcard():
    back_select_edit_row_button.grid_forget()
    add_flashcard_button.grid_forget()
    submit_flashcards_button.grid_forget()    
    row = [Label(second_frame, text="Term:"), Entry(second_frame), Label(second_frame, text="Definition:"), Text(second_frame, height=10, width=50)]
    delete_flashcard_button = Button(second_frame, text="Delete", command=lambda: delete_flashcard(row))
    row.append(delete_flashcard_button)
    for i in range(len(row)):
        row[i].grid(row=len(flashcard_rows), column=i*3, columnspan=3)
    flashcard_rows.append(row)
    back_select_edit_row_button.grid(row=len(flashcard_rows), column=0, columnspan=4)
    add_flashcard_button.grid(row=len(flashcard_rows), column=4, columnspan=4)
    submit_flashcards_button.grid(row=len(flashcard_rows), column=8, columnspan=4)    

def back_select_edit_row():
    for row in flashcard_rows:
        for w in row:
            w.grid_forget()
    back_select_edit_row_button.grid_forget()
    add_flashcard_button.grid_forget()
    submit_flashcards_button.grid_forget()
    edit_set_label.grid(row=0, column=0)
    selected_set_dropdown.grid(row=0, column=1)
    return_home_button.grid(row=1, column=0)
    edit_set_button.grid(row=1, column=1)    

def create_set():
    global set_name_label
    global set_name_entry
    global return_home_button
    global submit_set_button
    create_set_button.grid_forget()
    select_edit_set_button.grid_forget()
    select_study_set_button.grid_forget()   
    select_delete_set_button.grid_forget()
    set_name_label = Label(second_frame, text="New Set Name:")
    set_name_entry = Entry(second_frame)
    return_home_button = Button(second_frame, text="Return Home", command=return_home)
    submit_set_button = Button(second_frame, text="Submit New Set", command=submit_set)
    set_name_label.grid(row=0, column=0)
    set_name_entry.grid(row=0, column=1)
    return_home_button.grid(row=1, column=0)
    submit_set_button.grid(row=1, column=1)
    
def delete_flashcard(row, flashcard=None):
    return
    
def edit_set():
    global selected_set
    global flashcard_rows
    global back_select_edit_row_button
    global add_flashcard_button
    global submit_flashcards_button
    root.geometry("1000x400")
    edit_set_label.grid_forget()
    selected_set_dropdown.grid_forget()
    return_home_button.grid_forget()
    edit_set_button.grid_forget() 
    selected_set = Set(selected_set_var.get())
    flashcard_rows = []
    for flashcard in selected_set.flashcards:
        term_entry = Entry(second_frame)
        term_entry.insert(0, flashcard.term)
        definition_entry = Text(second_frame, height=10, width=50)
        definition_entry.insert("1.0", flashcard.definition)
        row = [Label(second_frame, text="Term:"), 
               term_entry, 
               Label(second_frame, text="Definition:"), 
               definition_entry]
        delete_flashcard_button = Button(second_frame, text="Delete", command=lambda: delete_flashcard(row, flashcard=flashcard))
        row.append(delete_flashcard_button)
        flashcard_rows.append(row)
    row = [Label(second_frame, text="Term:"), Entry(second_frame), Label(second_frame, text="Definition:"), Text(second_frame, height=10, width=50)]
    delete_flashcard_button = Button(second_frame, text="Delete", command=lambda: delete_flashcard(row))
    row.append(delete_flashcard_button)
    flashcard_rows.append(row)
    for i in range(len(flashcard_rows)):
        for j in range(len(flashcard_rows[i])):
            flashcard_rows[i][j].grid(row=i, column=j*3, columnspan=3)
    back_select_edit_row_button = Button(second_frame, text="<< Back", command=back_select_edit_row)
    add_flashcard_button = Button(second_frame, text="Add Flashcard", command=add_flashcard)
    submit_flashcards_button = Button(second_frame, text="Submit Flashcards", command=submit_flashcards)
    back_select_edit_row_button.grid(row=len(flashcard_rows), column=0, columnspan=4)
    add_flashcard_button.grid(row=len(flashcard_rows), column=4, columnspan=4)
    submit_flashcards_button.grid(row=len(flashcard_rows), column=8, columnspan=4)
    
def return_home():
    try:
        set_name_label.grid_forget()
        set_name_entry.grid_forget()
        return_home_button.grid_forget()
        submit_set_button.grid_forget()  
    except NameError:
        pass
    try:
        selected_set_dropdown.grid_forget() 
        return_home_button.grid_forget() 
        edit_set_button.grid_forget() 
        edit_set_label.grid_forget()   
    except NameError:
        pass
    create_set_button.grid(row=0, column=0)
    select_edit_set_button.grid(row=1, column=0)
    select_study_set_button.grid(row=2, column=0) 
    select_delete_set_button.grid(row=3, column=0)
    
def select_delete_set():
    return

def select_edit_set():
    global selected_set_var
    global selected_set_dropdown
    global return_home_button
    global edit_set_button
    global edit_set_label
    create_set_button.grid_forget()
    select_edit_set_button.grid_forget()
    select_study_set_button.grid_forget() 
    select_delete_set_button.grid_forget()
    edit_set_label = Label(second_frame, text="Edit Set:")
    databases = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.db'):
            file = file.replace('.db','')
            databases.append(file)
    selected_set_var = StringVar()
    selected_set_dropdown = OptionMenu(second_frame, selected_set_var, *databases)
    return_home_button = Button(second_frame, text="Return Home", command=return_home)
    edit_set_button = Button(second_frame, text="Edit Set", command=edit_set)
    edit_set_label.grid(row=0, column=0)
    selected_set_dropdown.grid(row=0, column=1)
    return_home_button.grid(row=1, column=0)
    edit_set_button.grid(row=1, column=1)

def select_study_set():
    return

def submit_flashcards():
    return

def submit_set():
    global selected_set
    selected_set = Set(set_name_entry.get())
    return_home()

create_set_button = Button(second_frame, text="Create Set", command=create_set)
select_edit_set_button = Button(second_frame, text="Edit Set", command=select_edit_set)
select_study_set_button = Button(second_frame, text="Study Set", command=select_study_set)
select_delete_set_button = Button(second_frame, text="Delete Set", command=select_delete_set)

create_set_button.grid(row=0, column=0)
select_edit_set_button.grid(row=1, column=0)
select_study_set_button.grid(row=2, column=0)
select_delete_set_button.grid(row=3, column=0)

root.mainloop()