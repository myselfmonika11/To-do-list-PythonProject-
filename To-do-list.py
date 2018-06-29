from tkinter import *
from tkinter import messagebox
import random

root=Tk()

root.config(bg="#E7C333")

root.minsize(width=300,height=500)
root.maxsize(width=300,height=500)

root.title("My To Do List")

root.geometry("300x500")

tasks=[]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")
    
def add_task():
    task=txt_input.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showinfo("Warning","You need to enter a task!!")
    txt_input.delete(0,"end")
    
def del_all():
    confirmed=messagebox.askyesno("message","Do you really want to delete it all?")
    if confirmed == True:
        global tasks
        tasks=[]
        update_listbox()
    
def del_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()
    
def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    task=random.choice(tasks)
    messagebox.showinfo("Random no.",task)
    
def show_number_of_tasks():
    number_of_tasks=len(tasks)
    msg="Number of tasks: %s" %number_of_tasks
    lbl_display["text"]=msg

def exit():
    confirmed=messagebox.askyesno("ques","Do you want to exit?")
    if confirmed==True:
        global tasks
        tasks=[]
        root.destroy()
    

lbl_title=Label(root,text="To Do List",bg="white",font="bold")
lbl_title.grid(row=0,column=0,padx=20,pady=20)

lbl_display=Label(root,text="",bg="#E7C333")
lbl_display.grid(row=0,column=1)

txt_input=Entry(root,width=20)
txt_input.grid(row=1,column=1)

btn_add_task=Button(root,text="Add task",fg="green",bg="white",command=add_task,width=13)
btn_add_task.grid(row=1,column=0,pady=10)

btn_del_all=Button(root,text="Delete all task",fg="green",bg="white",command=del_all,width=13)
btn_del_all.grid(row=2,column=0,pady=10)

btn_del_one=Button(root,text="Delete",fg="green",bg="white",command=del_one,width=13)
btn_del_one.grid(row=3,column=0,pady=10)

btn_sort_asc=Button(root,text="Sort(ASC)",fg="green",bg="white",command=sort_asc,width=13)
btn_sort_asc.grid(row=4,column=0,pady=10)

btn_sort_desc=Button(root,text="Sort(DESC)",fg="green",bg="white",command=sort_desc,width=13)
btn_sort_desc.grid(row=5,column=0,pady=10)

btn_choose_random=Button(root,text="Choose Random",fg="green",bg="white",command=choose_random,width=13)
btn_choose_random.grid(row=6,column=0,pady=10)

btn_number_of_tasks=Button(root,text="Number of Tasks",fg="green",bg="white",command=show_number_of_tasks,width=13)
btn_number_of_tasks.grid(row=7,column=0,pady=10)

btn_exit=Button(root,text="Exit",fg="green",bg="white",command=exit,width=13)
btn_exit.grid(row=8,column=0,pady=10)

lb_tasks=Listbox(root,height=12)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()
