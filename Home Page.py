import tkinter as tk

window=tk.Tk()
window.geometry("1350x700+0+0")
window.title("Student Management System Home Page")
window.config(bg="Pink")

title_label=tk.Label(window,text="!!Welcome!!",font=("Times New Roman",30,"bold"),border=15,relief=tk.GROOVE,bg="Pink",foreground="Black")
title_label.pack(side=tk.TOP,fill=tk.X)
detail_frame = tk.LabelFrame(window,text="Student Management System",font=("Times New Roman",48,"bold"),fg="Black",bd=12,relief=tk.GROOVE,bg="Pink")
detail_frame.place(x=240,y=260,width=850,height=150)

btn_frame=tk.Frame(window,bg="Pink",relief=tk.GROOVE,bd=10,command=main_page)
btn_frame.place(x=560,y=420,width=195,height=65)
continue_btn=tk.Button(btn_frame,text="Continue",bd=7,font=("Times New Roman",13),width=17)
continue_btn.grid(row=0,column=0,padx=2,pady=2)
