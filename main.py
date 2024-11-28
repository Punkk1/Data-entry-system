import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

def enter_data():
    accepted=accept_var.get()

    if accepted=="Accepted":


        firstname=first_name_entry.get()
        lastname=last_name_entry.get()

        if firstname and lastname:

            title=title_combobox.get()
            age=age_spinbox.get()
            nationality=nationality_entry.get()

            numcourses=numcourses_spinbox.get()
            numsemesters=numsemesters_spinbox.get()

            reg_status=reg_status_var.get()
            

            
            print("\nFirst name: ",firstname,"\nLast name: ",lastname)
            print("\nTitle: ",title,"\nAge: ",age,"\nNationality: ",nationality)
            print("\nCourses: ",numcourses,"\nSemester: ",numsemesters)
            print("\nRegistration Status ",reg_status)
            print("--------------------------------------------------------------")

            conn=sqlite3.connect('data.db')
            table_create_query='''CREATE TABLE IF NOT EXISTS Student_Data
                    (firstname TEXT,lastname TEXT,title TEXT,age INT,nationality TEXT,
                    registration_status TEXT,num_courses INT,num_semesters INT)
            '''
            conn.execute(table_create_query)

            data_insert_query='''INSERT INTO Student_Data(firstname,lastname,title,
            age,nationality,registration_status,num_courses,num_semesters)  VALUES
            (?,?,?,?,?,?,?,?)'''
            data_insert_tuple=(firstname,lastname,title,age,nationality,
                               reg_status,numcourses,numsemesters)
            cursor=conn.cursor()
            cursor.execute(data_insert_query,data_insert_tuple)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showwarning(title="Error",message="You have not entered the data")
    else:
        tkinter.messagebox.showwarning(title="Error",message="You have not accepted the terms")


window = tkinter.Tk()
window.title("Data entry form")
frame =tkinter.Frame(window)
frame.pack()

#saving user information
user_info_frame=tkinter.LabelFrame(frame, text="User Information",font='Ariel')
user_info_frame.grid(row=0,column=0,padx=20,pady=10)

first_name_label=tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label=tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_entry=tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame,values=["","Mr","Ms","Dr"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame ,from_=18, to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_entry=tkinter.Entry(user_info_frame)
nationality_label.grid(row=2,column=1)
nationality_entry.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

course_frame=tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

register_label=tkinter.Label(course_frame,text="Registration Status")

reg_status_var=tkinter.StringVar(value="Not Registered")
register_check=tkinter.Checkbutton(course_frame,text="Currently Registered",variable=reg_status_var,onvalue="Registered",offvalue="Not Registered")
register_check.grid(row=1,column=0)
register_label.grid(row=0,column=0)


numcourses_label=tkinter.Label(course_frame,text="Completed Courses")
numcourses_spinbox=tkinter.Spinbox(course_frame,from_=0, to='infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label=tkinter.Label(course_frame,text="Semesters")
numsemesters_spinbox=tkinter.Spinbox(course_frame,from_=1, to=8)
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

terms_frame=tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,padx=20,pady=10,sticky="news")

accept_var=tkinter.StringVar()
terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms & conditions",variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

button =tkinter.Button(frame,text="Enter Data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)






window.mainloop()