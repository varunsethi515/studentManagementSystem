import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import gender as gender
import pymysql
##pymysql, mysql.connector, squlites(modules use to connect date base)

##formation of the window

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")
win.config(bg="white")
##formation of the SMS lable at the top
title_label=tk.Label(win,text="||--------------------Student Management System--------------------||",font=("Times New Roman",30,"bold"),border=15,relief=tk.GROOVE,bg="pink",foreground="black")
title_label.pack(side=tk.TOP,fill=tk.X)
##formation of frame

##Detail_Frame
detail_frame = tk.LabelFrame(win,text="Enter the details of the Student",font=("Times New Roman",22,"bold"),fg="black",bd=12,relief=tk.GROOVE,bg="pink")
detail_frame.place(x=20,y=110,width=420,height=575)
##Data_Frame
data_frame = tk.LabelFrame(win,bd=12,bg="pink",relief=tk.GROOVE)
data_frame.place(x=475,y=110,width=830,height=575)

##Variables Start
rollno=tk.StringVar()
name=tk.StringVar()
department=tk.StringVar()
contactno=tk.StringVar()
mail=tk.StringVar()
address=tk.StringVar()
yearsemester=tk.StringVar()
dateofbirth=tk.StringVar()
gender=tk.StringVar()
## Vriable End

##Entry Start
rollno_lbl = tk.Label(detail_frame,text="Roll No.",fg="black",font=("Times New Roman",15),bg="Pink")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)
rollno_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name",fg="black",font=("Times New Roman",15),bg="Pink")
name_lbl.grid(row=1,column=0,padx=2,pady=2)
name_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

department_lbl=tk.Label(detail_frame,text="Department",fg="black",font=("Times New Roman",15),bg="Pink")
department_lbl.grid(row=2,column=0,padx=2,pady=2)
department_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=department)
department_ent.grid(row=2,column=1,padx=2,pady=2)

contactno_lbl=tk.Label(detail_frame,text="Contact No",fg="black",font=("Times New Roman",15),bg="Pink")
contactno_lbl.grid(row=3,column=0,padx=2,pady=2)
contactno_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=contactno)
contactno_ent.grid(row=3,column=1,padx=2,pady=2)

mail_lbl=tk.Label(detail_frame,text="Mail",fg="black",font=("Times New Roman",15),bg="Pink")
mail_lbl.grid(row=4,column=0,padx=2,pady=2)
mail_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=mail)
mail_ent.grid(row=4,column=1,padx=2,pady=2)

address_lbl=tk.Label(detail_frame,text="Address",fg="black",font=("Times New Roman",15),bg="Pink")
address_lbl.grid(row=5,column=0,padx=2,pady=2)
address_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=address)
address_ent.grid(row=5,column=1,padx=2,pady=2)

yearsemester_lbl=tk.Label(detail_frame,text="Year-Semester",fg="black",font=("Times New Roman",15),bg="Pink")
yearsemester_lbl.grid(row=6,column=0,padx=2,pady=2)
yearsemester_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=yearsemester)
yearsemester_ent.grid(row=6,column=1,padx=2,pady=2)

dob_lbl=tk.Label(detail_frame,text="Date of Birth",fg="black",font=("Times New Roman",15),bg="Pink")
dob_lbl.grid(row=7,column=0,padx=2,pady=2)
dob_ent=tk.Entry(detail_frame,bd=7,font=("Times New Roman",15),textvariable=dateofbirth)
dob_ent.grid(row=7,column=1,padx=2,pady=2)

##for gender we have to give option as M/F/O & state="readonly"
gender_lbl=tk.Label(detail_frame,text="Gender",fg="black",font=("Times New Roman",15),bg="Pink")
gender_lbl.grid(row=8,column=0,padx=2,pady=2)
gender_ent =ttk.Combobox(detail_frame,text="search",font=("Times New Roman",13),state="readonly",textvariable=gender)
gender_ent['values']=["Male","Female","Other"]
gender_ent.grid(row=8,column=1,padx=2,pady=2)
##Entery End

##Function Start
def fetch_data():
   conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
   curr = conn.cursor()
   curr.execute("SELECT *FROM data")
   rows = curr.fetchall()
   if len(rows)!=0:
      student_table.delete(*student_table.get_children())
      for row in rows:
         student_table.insert('',tk.END,values=row)
      conn.commit()
   conn.close()

def add_fun():
      '''This fucntion will add the information given by the user to the university database'''
      conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
      curr = conn.cursor()
      curr.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),department.get(),contactno.get(),mail.get(),address.get(),yearsemester.get(),dateofbirth.get(),gender.get()))
      conn.commit()
      fetch_data()
      clear_fun()
      conn.close()

def get_cursor(event):
    '''This function will fetch the data of the selected row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    department.set(row[2])
    contactno.set(row[3])
    mail.set(row[4])
    address.set(row[5])
    yearsemester.set(row[6])
    dateofbirth.set(row[7])
    gender.set(row[8])

def clear_fun():
    '''This function will clear the entry box'''
    rollno.set("")
    name.set("")
    department.set("")
    contactno.set("")
    mail.set("")
    address.set("")
    yearsemester.set("")
    dateofbirth.set("")
    gender.set("")

def update_fun():
    '''This function will update data according to the user '''
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
    curr = conn.cursor()
    curr.execute("update data set name=%s,department=%s,contactno=%s,mail=%s,address=%s,yearsemester=%s,dateofbirth=%s,gender=%s where rollno=%s",(name.get(),department.get(),contactno.get(),mail.get(),address.get(),yearsemester.get(),dateofbirth.get(),gender.get(),rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear_fun()

def delete_fun():
    '''This function will delete the record from ur database'''
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms")
    curr = conn.cursor()
    curr.execute("delete from data where rollno=%s",rollno.get())
    conn.commit()
    conn.close()
    fetch_data()
    clear_fun()

##Function End

##Button Start
btn_frame=tk.Frame(detail_frame,bg="Pink",relief=tk.GROOVE,bd=10)
btn_frame.place(x=15,y=390,width=370,height=120)

add_btn=tk.Button(btn_frame,text="Add",bd=7,font=("Times New Roman",13),width=17,command=add_fun)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_frame,text="Update",bd=7,font=("Times New Roman",13),width=17,command=update_fun)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn=tk.Button(btn_frame,text="Delete",bd=7,font=("Times New Roman",13),width=17,command=delete_fun)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn=tk.Button(btn_frame,text="Clear",bd=7,font=("Times New Roman",13),width=17,command=clear_fun)
clear_btn.grid(row=1,column=1,padx=2,pady=2)
##Button End

##Search Frame Start
search_frame=tk.Frame(data_frame,bg="Pink",relief=tk.GROOVE,bd=10)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search",bg="Pink",font=("Times New Roman",13))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,text="Search",font=("Times New Roman",13),state="readonly")
search_in['values']=["Name","Roll No","Department","yearsemester"]
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Times New Roman",13))
search_btn.grid(row=0,column=2,padx=30,pady=2)

showall_btn=tk.Button(search_frame,text="Show All",font=("Times New Roman",13))
showall_btn.grid(row=0,column=3,padx=250,pady=2)
##Search Frame End

##Database Frame Start
main_frame=tk.Frame(data_frame,bg="pink",relief=tk.GROOVE,bd=11)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Roll No","Name","Department","Contact No","Mail","Address","Year-Semester","Date-of-Birth","Gender"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)
y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

##Heading
student_table.heading("Roll No",text="Roll No")
student_table.heading("Name",text="Name")
student_table.heading("Date-of-Birth",text="Date-of-Birth")
student_table.heading("Department",text="Department")
student_table.heading("Year-Semester",text="Year-Semester")
student_table.heading("Contact No",text="Contact No")
student_table.heading("Mail",text="Mail")
student_table.heading("Gender",text="Gender")
student_table.heading("Address",text="Address")

student_table['show']='headings'

student_table.column("Roll No",width=100)
student_table.column("Name",width=100)
student_table.column("Date-of-Birth",width=100)
student_table.column("Department",width=100)
student_table.column("Year-Semester",width=100)
student_table.column("Contact No",width=100)
student_table.column("Mail",width=150)
student_table.column("Gender",width=100)
student_table.column("Address",width=150)
student_table.pack(fill=tk.BOTH,expand=True)
##Database Frame End

fetch_data()
student_table.bind("<ButtonRelease-1>",get_cursor)
win.mainloop()
