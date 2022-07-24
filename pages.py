from tkinter import *
from tkinter import messagebox
from urllib.parse import _ParseResultBase
from databasfunction import login as logindb,serachname as sn,adduser as adu,getinformation as gi

from funct import center,name
from PIL import ImageTk, Image
from time import sleep

class loginpage:
    
    def __init__(self,root):
        
        root.config(bg="#202020")
        root.geometry('800x520')
        center(root)
        root.overrideredirect(1)
        self.root=root
        #frame
        self.frame1 = Frame(root, width=800, height=500,background="#202020")
        self.frame1.pack()
        self.frame1.config(bg="#202020")


        self.image = Image.open("source/login.jpg")
    
        # Resize the image using resize() method
        self.resize_image = self.image.resize((200,200))
        
        self.img = ImageTk.PhotoImage(self.resize_image)

        # create label and add resize image
        self.labelx = Label(self.frame1,text="",image=self.img)
        self.labelx.config(bg= "#202020", fg= "#202020")
        self.labelx.image = self.img
        self.labelx.place(x=305,y=0)
        
        self.namelb=Label(root,text="name",font=("Arial", 30),bg= "#202020",fg="white")
        self.namelb.place(x=120,y=200)

        self.ename=Entry(root,width=15,font=("Arial", 30))
        self.ename.place(x=320,y=200)

        self.passlab=Label(root,text="password",font=("Arial", 30),bg= "#202020",fg="white")
        self.passlab.place(x=120,y=290)

        self.epass=Entry(root,width=15,font=("Arial", 30),show="*")
        self.epass.place(x=320,y=290)

        self.bt=Button ( root,text ="Login",font=("Arial", 30),command=lambda:self.login())#""",command=lambda:loginsys(root,ename,epass,label1,namelb,passlab,bt)""")
        self.bt.place(x=340,y=380)
        self.bt1=Button ( root,fg="white",bg="#202020",text ="create account",relief=FLAT,font=("Arial", 18),command=lambda:self.register())#""",command=lambda:loginsys(root,ename,epass,label1,namelb,passlab,bt)""")
        self.bt1.place(x=315,y=470)
    def login(self):
        if(logindb(self.ename.get(),self.epass.get())):
            messagebox.showinfo("login","login succasfull")
            self.name=self.ename.get()
            self.destroy()
            
            return home_page(self.root,self.name)
        else:
            messagebox.showerror("error","name or password is wrong")
            self.ename.delete(0, 'end')
            self.epass.delete(0, 'end')
    def register(self):
        self.destroy()
        return register(self.root)
    
    def destroy(self):
        self.frame1.destroy()
        self.labelx.destroy()
        self.namelb.destroy()
        self.ename.destroy()
        self.passlab.destroy()
        self.epass.destroy()
        self.bt.destroy()
        self.bt1.destroy()
class register:
    def __init__(self,root):
        self.addx=50
        self.wdx=12
        root.config(bg="#202020")
        root.geometry('900x520')
        center(root)
        root.overrideredirect(1)
        self.root=root
        #frame
        self.frame1 = Frame(root, width=800, height=500,background="#202020")
        self.frame1.pack()
        self.frame1.config(bg="#202020")


        self.image = Image.open("source/login.jpg")
    
        # Resize the image using resize() method
        self.resize_image = self.image.resize((200,200))
        
        self.img = ImageTk.PhotoImage(self.resize_image)

        # create label and add resize image
        self.label1 = Label(self.frame1,text="",image=self.img)
        self.label1.config(bg= "#202020", fg= "#202020")
        self.label1.image = self.img
        self.label1.place(x=305,y=0)

        self.namelb=Label(root,text="name:",font=("Arial", 30),bg= "#202020",fg="white")
        self.namelb.place(x=20,y=200)

        self.ename=Entry(root,width=self.wdx,font=("Arial", 30))
        self.ename.place(x=135,y=200)
        
        self.name2=Label(root,text="sec name:",font=("Arial", 30),bg= "#202020",fg="white")
        self.name2.place(x=370+self.addx,y=200)

        self.ename2=Entry(root,width=self.wdx,font=("Arial", 30))
        self.ename2.place(x=560+self.addx,y=200)

        self.passlab=Label(root,text="pass :",font=("Arial", 30),bg= "#202020",fg="white")
        self.passlab.place(x=20,y=310)

        self.epass=Entry(root,width=self.wdx,font=("Arial", 30),show="*")
        self.epass.place(x=135,y=310)

        self.passlab2=Label(root,text="conf pass:",font=("Arial", 30),bg= "#202020",fg="white")
        self.passlab2.place(x=370+self.addx,y=310)

        self.epass2=Entry(root,width=self.wdx,font=("Arial", 30),show="*")
        self.epass2.place(x=560+self.addx,y=310)

        self.b1=Button(root,text="create account",font=("Arial", 30),command=lambda:self.createaccount())
        self.b1.place(x=300,y=410)
        self.b2=Button(root,text="back",font=("Arial", 30),command=lambda:self.back())
        self.b2.place(x=0,y=0)
    def createaccount(self):
        print(sn(self.ename.get()))
        if(not name(self.ename.get(),5)):
            messagebox.showerror("error","name is string number length=>5")
            return False
        if(not name(self.ename2.get(),5)):
            messagebox.showerror("error","second name is string number length=>5")
            return False
        if(not name(self.epass.get(),6)):
            messagebox.showerror("error","pass is string number length>6")
            return False
        if(self.epass.get()!=self.epass2.get()):
            messagebox.showerror("error","conf pass = pass")
            return False
        if(sn(self.ename.get())):
            messagebox.showerror("error","user exist")
            return False
        adu(self.ename.get(),self.ename2.get(),self.epass.get())
        messagebox.showinfo("login","user added")
        self.destroy()
        return loginpage(self.root)
    def verifenotvide(self,b):
        return b.get()==""
    def back(self):
        self.destroy()
        return loginpage(self.root)
    def destroy(self):
        self.frame1.destroy()
        self.namelb.destroy()
        self.label1.destroy()
        self.ename.destroy()
        self.name2.destroy()
        self.ename2.destroy()
        self.epass.destroy()
        self.epass2.destroy()
        self.passlab.destroy()
        self.passlab2.destroy()
        self.b1.destroy()
        self.b2.destroy()
class home_page:
    
    def __init__(self,root,name):
        self.state=True
        self.name=name
        self.t=gi(name)
        root.config(bg="#202020")
        root.geometry('800x520')
        center(root)
        root.overrideredirect(1)
        self.root=root
        self.namelb=Label(root,text="name              :",font=("Arial", 30),bg= "#202020",fg="white")
        self.namelb.place(x=20,y=150)
        self.namelbent=Entry(root,width=15,font=("Arial", 30))  
        self.namelbent.place(x=300,y=150)

        self.secnamelb=Label(root,text="second name  :",font=("Arial", 30),bg= "#202020",fg="white")
        self.secnamelb.place(x=20,y=250)
        self.secnamelbent=Entry(root,width=15,font=("Arial", 30))  
        self.secnamelbent.place(x=300,y=250)

        self.passlb=Label(root,text="password        :",font=("Arial", 30),bg= "#202020",fg="white")
        self.passlb.place(x=20,y=350)
        self.passlbent=Entry(root,width=15,font=("Arial", 30))  
        self.passlbent.place(x=300,y=350)
        self.sh=Button(root,text ="show",font=("Arial", 20),command=lambda:self.show_hide())
        self.sh.place(x=640,y=345)
        self.bt=Button(root,text ="Log out",font=("Arial", 30),command=lambda:self.destroy())
        self.bt.place(x=0,y=0)
        self.enterdate()
    def enterdate(self):
            self.namelbent.insert(0,self.name)
            self.namelbent.configure(state='readonly')
            self.secnamelbent.insert(0,self.t[0])
            self.secnamelbent.configure(state='readonly')
            self.passlbent.insert(0,"*"*len(self.t[1]))
            self.passlbent.configure(state='readonly')
    def show_hide(self):
        self.passlbent.config(state=NORMAL)
        if(self.state):
            self.sh.config(text="hide")
            self.passlbent.delete(0, END)
            self.passlbent.insert(0,self.t[1])
            
        else:
            self.sh.config(text="show")
            self.passlbent.delete(0, END)
            self.passlbent.insert(0,"*"*len(self.t[1]))
        self.state=not self.state
        self.passlbent.config(state='readonly')
    def destroy(self):
            self.namelb.destroy()
            self.namelbent.destroy()
            self.secnamelb.destroy()
            self.secnamelbent.destroy()
            self.passlb.destroy()
            self.passlbent.destroy()
            self.bt.destroy()
            return loginpage(self.root)      