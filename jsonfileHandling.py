from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

import os
root=Tk()
# root.state("zoomed")
root.geometry("1300x500")
root.maxsize(width=1300,height=500)
root.minsize(width=1300,height=500)
root.title("Employees personal Data")

def loadjson():
     if os.path.exists("empDataFile.json") and os.path.getsize("empDataFile.json")>0:
          with open("empDataFile.json","r") as file:
               empData=json.load(file)
          
          for item in tree_table.get_children():
               tree_table.delete(item)
          for em in empData:
               et=tuple(tuple(empData[em].values()))
               tree_table.insert("", "end" ,text=em,values=et)

def Save():
     data_list=(entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get())
     emp_dct={}
     if os.path.exists("empDataFile.json") and os.path.getsize("empDataFile.json")>0:
          with open("empDataFile.json","r") as file:
               emp_dct=json.load(file)
     emp_dct[(f"emp{len(emp_dct)+1}")]={"Emp_name":data_list[0],"FatherName":data_list[1],"City":data_list[2],"PhoneNumber":data_list[3],"Desigination":data_list[4],"Department":data_list[5]}
     with open("empDataFile.json","w") as filew:
          json.dump(emp_dct,filew,indent=4)

     # tree_table.insert("","end",values=data_list)
     loadjson()
     for e in entries:
          e.delete(0,END)
def Update():
      
     if tree_table.selection():
          data_list=(entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get())
          emp_dct={}
          if os.path.exists("empDataFile.json") and os.path.getsize("empDataFile.json")>0:
               with open("empDataFile.json","r") as file:
                    emp_dct=json.load(file)
          emp_dct[tree_table.item(tree_table.selection(),"text")]={"Emp_name":data_list[0],"FatherName":data_list[1],"City":data_list[2],"PhoneNumber":data_list[3],"Desigination":data_list[4],"Department":data_list[5]}       
          with open("empDataFile.json","w") as filew:
               json.dump(emp_dct,filew,indent=4)
          loadjson()
          for e in entries:
               e.delete(0,END)
     else:
          messagebox.showinfo("Message","Kindly select any row to update form table First!")
          
def Delete():
     pass
def Search():
     pass
def Cancel():
     pass
def select_row(event):
     for i,e in enumerate(entries):
          e.delete(0,END)
          e.insert(0,tree_table.set(tree_table.selection(),list[i]))






button_commands = {"Save":Save,"Update":Update,"Delete":Delete,"Search":Search,"Cancel":Cancel}
entries=[]
list=["Emp_Name","Father Name","City","Phone Number","Desigination","Department"]
entryframe=Frame(root,bd=1,relief="solid")
# created heading of table

tree_table=ttk.Treeview(entryframe,show="headings",columns=tuple(list))

for i,l_name in enumerate(list):
        tree_table.column(l_name,width=100,anchor="center")
        tree_table.heading(l_name,text=l_name)




#start creating rows here
tree_table.pack(fill=BOTH,side="top")
scroll=Scrollbar(root,command=tree_table.yview)

tree_table.configure(yscrollcommand=scroll.set)
#start loading data in tree from json file
loadjson()

tree_table.bind("<<TreeviewSelect>>",select_row)
entryframe.grid(row=0,column=0)
 
# data entry form creation
form_frame=Frame(root,bd=1,relief="solid")
entry_names=()
for i,e_name in enumerate(list):
    entry_lbl=Label(form_frame,bd=1,relief="sunken",width=25,text=e_name,font=("Arial",15,"bold"))
    etry = Entry(form_frame,bd=2,relief="groove",font=("Arial", 11),highlightthickness=1,highlightbackground="gray",highlightcolor="blue")
    entry_lbl.grid(row=i,column=0,padx=2,pady=2)
    etry.grid(row=i,column=1,padx=2,pady=2,ipady=8,ipadx=20)
    entries.append(etry)


for i,b_name in enumerate(button_commands):
    
    button_obj=Button(form_frame,bd=1,font=("Arial",11,"bold"),text=b_name,width=10,command=button_commands[b_name])
    if i<=2:
        button_obj.grid(row=8,column=i,ipadx=15,ipady=8)
    else:
        button_obj.grid(row=9,column=i-3,ipadx=15,ipady=8)
    

form_frame.grid(row=0,column=1)


root.mainloop()