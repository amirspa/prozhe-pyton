# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter
import json
def submit():
    lbl3.configure(text="")
    f = open("data.json")
    karbaran = json.load(f)
    user = en1.get()
    alamat=["!","@","$","%","*","_"," ",".",",","~","#","&","(",")","^","/","'",'"',"+","-","|"]
    if user in karbaran:
        lbl3.configure(text="tekrari")
    else:
        if len(user)>10 or len(user)<3:
            
            lbl3.configure(text="type more or less")
        else:
            for i in user:
                if i in alamat:
                    lbl3.configure(text="just number")
                else:
                    lbl3.configure(text="done")
                    user1={en1.get():en2.get()}
                    
                    with open('data.json') as file:
                        data=json.load(file)
                    with open('data.json','w') as file:
                        data.update(user1)
                        file.seek(0)
                        json.dump(data,file)
            
def login():
    username=en1.get()
    password=en2.get()
    f = open("data.json")
    karbaran = json.load(f)
    if username in karbaran:
        if karbaran[username]==password:
            lbl3.configure(text="welcome")
        else:
            lbl3.configure(text="error")
    else:
        lbl3.configure(text="first ")
    

win =tkinter.Tk()
win.geometry("450x100")

# ------- widgets -------
lbl1=tkinter.Label(win,text="username:")
lbl2=tkinter.Label(win,text="password:")
en1=tkinter.Entry(win)
en2=tkinter.Entry(win)
lbl3=tkinter.Label(win,text="")
b1 =tkinter.Button(win,text="Submit",command=submit)
b2 =tkinter.Button(win,text="login",command=login)
# - ------grids ---------
lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=1)
en1.grid(row=1,column=0)
en2.grid(row=1,column=1)
lbl3.grid(row=1,column=2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

win.mainloop()
