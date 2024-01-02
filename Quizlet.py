from Set import Set
from tkinter import *
from tkinter import ttk
import os

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
my_canvas.bind('<MouseWheel>', lambda event: my_canvas.yview_scroll(int(event.delta/60), "units"))
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
    
def back_select_study_row():
    for w in flashcard_widgets[0]:
        w.grid_forget()
    star_label.grid_forget()
    study_set_label.grid(row=0, column=0)
    selected_set_dropdown.grid(row=0, column=1)
    return_home_button.grid(row=1, column=0)
    study_set_button.grid(row=1, column=1)      

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
    for w in row:
        w.grid_forget()
    flashcard_rows.remove(row)
    if flashcard != None:
        selected_set.remove(flashcard)
    
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
        delete_flashcard_button = Button(second_frame, text="Delete", command=lambda card=flashcard, r=row: delete_flashcard(r, flashcard=card))
        row.append(delete_flashcard_button)
        flashcard_rows.append(row)
    empty_row = [Label(second_frame, text="Term:"), Entry(second_frame), Label(second_frame, text="Definition:"), Text(second_frame, height=10, width=50)]
    delete_flashcard_button = Button(second_frame, text="Delete", command=lambda: delete_flashcard(empty_row))
    empty_row.append(delete_flashcard_button)
    flashcard_rows.append(empty_row)
    for i in range(len(flashcard_rows)):
        for j in range(len(flashcard_rows[i])):
            flashcard_rows[i][j].grid(row=i, column=j*3, columnspan=3)
    back_select_edit_row_button = Button(second_frame, text="<< Back", command=back_select_edit_row)
    add_flashcard_button = Button(second_frame, text="Add Flashcard", command=add_flashcard)
    submit_flashcards_button = Button(second_frame, text="Submit Flashcards", command=submit_flashcards)
    back_select_edit_row_button.grid(row=len(flashcard_rows), column=0, columnspan=4)
    add_flashcard_button.grid(row=len(flashcard_rows), column=4, columnspan=4)
    submit_flashcards_button.grid(row=len(flashcard_rows), column=8, columnspan=4)
    
def end_study():
    global end_study_label
    global previous_flashcard_button
    global review_starred_terms_button
    global return_home_button
    global star_label
    for w in flashcard_widgets[len(flashcard_widgets)-1]:
        w.grid_forget()
    star_label.grid_forget()
    end_study_label = Label(second_frame, text="You've reviewed all flashcards. What would you like to do next?")
    previous_flashcard_button = Button(second_frame, text="<< Back", command=lambda card=flashcards[len(flashcards)-1]: study_flashcard(card))
    review_starred_terms_button = Button(second_frame, text="Review Starred Terms", command=review_starred_terms)
    return_home_button = Button(second_frame, text="Return Home", command=return_home)
    end_study_label.grid(row=0, column=0, columnspan=3)
    previous_flashcard_button.grid(row=1, column=0)
    review_starred_terms_button.grid(row=1, column=1)
    return_home_button.grid(row=1, column=2)

def flip_flashcard(event, index):
    current_text = flashcard_widgets[index][0].cget("text")
    flashcard_widgets[index][0].config(text="")
    if current_text == flashcards[index].definition:
        flashcard_widgets[index][0].config(text=flashcards[index].term)
    else:
        flashcard_widgets[index][0].config(text=flashcards[index].definition)
    
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
    try:
        for row in flashcard_rows:
            for w in row:
                w.grid_forget()
        back_select_edit_row_button.grid_forget()
        add_flashcard_button.grid_forget()
        submit_flashcards_button.grid_forget()
    except NameError:
        pass
    try:
        selected_set_dropdown.grid_forget() 
        return_home_button.grid_forget() 
        study_set_button.grid_forget() 
        study_set_label.grid_forget()   
    except NameError:
        pass    
    try:
        end_study_label.grid_forget()
        previous_flashcard_button.grid_forget()
        review_starred_terms_button.grid_forget()
        return_home_button.grid_forget()      
    except NameError:
        pass    
    create_set_button.grid(row=0, column=0)
    select_edit_set_button.grid(row=1, column=0)
    select_study_set_button.grid(row=2, column=0) 
    select_delete_set_button.grid(row=3, column=0)
    
def review_starred_terms():
    return
    
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
    global selected_set_var
    global selected_set_dropdown
    global return_home_button
    global study_set_button
    global study_set_label
    create_set_button.grid_forget()
    select_edit_set_button.grid_forget()
    select_study_set_button.grid_forget() 
    select_delete_set_button.grid_forget()
    study_set_label = Label(second_frame, text="Study Set:")
    databases = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.db'):
            file = file.replace('.db','')
            databases.append(file)
    selected_set_var = StringVar()
    selected_set_dropdown = OptionMenu(second_frame, selected_set_var, *databases)
    return_home_button = Button(second_frame, text="Return Home", command=return_home)
    study_set_button = Button(second_frame, text="Study Set", command=study_set)
    study_set_label.grid(row=0, column=0)
    selected_set_dropdown.grid(row=0, column=1)
    return_home_button.grid(row=1, column=0)
    study_set_button.grid(row=1, column=1) 
    
def study_flashcard(card):
    global star_label
    try:
        for w in flashcard_widgets[flashcards.index(card)-1]:
            w.grid_forget()
        star_label.grid_forget()
    except (IndexError, NameError):
        pass
    try:
        end_study_label.grid_forget()
        previous_flashcard_button.grid_forget()
        review_starred_terms_button.grid_forget()
        return_home_button.grid_forget() 
    except NameError:
        pass
    star_label = Label(second_frame, text="Star:")
    flashcard_widgets[flashcards.index(card)][0].grid(row=0, column=0, columnspan=4)
    flashcard_widgets[flashcards.index(card)][1].grid(row=1, column=0)
    star_label.grid(row=1, column=1)
    flashcard_widgets[flashcards.index(card)][2].grid(row=1, column=2)
    flashcard_widgets[flashcards.index(card)][3].grid(row=1, column=3)
    
def study_set():
    global selected_set
    global flashcard_widgets
    global star_vars
    global flashcards
    study_set_label.grid_forget()
    selected_set_dropdown.grid_forget()
    return_home_button.grid_forget()
    study_set_button.grid_forget()
    selected_set = Set(selected_set_var.get())
    flashcards = selected_set.getShuffledFlashcards()
    flashcard_widgets = []
    star_vars = []
    for i in range(len(flashcards)):
        star_vars.append(IntVar())
        widgets = [
            Label(second_frame, text=flashcards[i].definition),
            Button(second_frame, text="<< Back"),
            Checkbutton(second_frame, var=star_vars[i], onvalue=1, offvalue=0),
            Button(second_frame, text="Next >>")
            ]
        widgets[0].bind("<Button-1>", lambda event, i=i: flip_flashcard(event, i))
        if i == 0:
            widgets[1].config(command=back_select_study_row)
        else:
            widgets[1].config(command=lambda i=i: study_flashcard(flashcards[i-1]))
        if i == len(flashcards) - 1:
            widgets[3].config(command=end_study)
        else:
            widgets[3].config(command=lambda i=i: study_flashcard(flashcards[i+1]))
        flashcard_widgets.append(widgets)
    study_flashcard(flashcards[0])

def submit_flashcards():
    flashcard_tuples = []
    for row in flashcard_rows:
        flashcard_tuples.append((row[1].get(), row[3].get('1.0', END).replace('\n','')))
    selected_set.update(flashcard_tuples)
    return_home()

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