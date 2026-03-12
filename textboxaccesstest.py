from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x600")
def func():
    messagebox.showinfo("ok","Function is running")
    Label(root,text=entries[0].get()).pack()
list=["save","delete"]
entries=[]
for i,txt_box in enumerate(list):
    box=Entry(root,bd=1)
    box.pack()
    entries.append(box)
Button(root,text="OK",height=5,width=15,command=func).pack()
root.mainloop()