from tkinter import ttk
import tkinter as tk

class ElementFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        
        self.__elementName = tk.StringVar(self.master,"")
        self.__elementUser = tk.StringVar(self.master,"")
        self.__elementPassword = tk.StringVar(self.master,"")
        self.__elementComment = tk.StringVar(self.master,"")
        
        
        ttk.Label(self,textvariable=self.__elementName,font=25).pack(pady=10)

        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp, text="User",width=12,anchor="e").pack(side="left",padx=3)
        ttk.Entry(temp,textvariable=self.__elementUser,width=40,state="disabled").pack(side="left",padx=3)
        ttk.Button(temp,text="Copy", width=5,command=lambda:self.__clipButton(self.__elementUser.get())).pack(side="right",padx=3)
        

        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp, text="Password",width=12,anchor="e").pack(side="left",padx=3)
        pwdEntry = ttk.Entry(temp,textvariable=self.__elementPassword,width=40,state="disabled")

        def showPwd(event):
            pwdEntry["show"] = ""

        def hidePwd(event):
            pwdEntry["show"] = "*"

        pwdEntry["show"] = "*"
        pwdEntry.bind("<Leave>",hidePwd)
        pwdEntry.bind("<Button-1>", showPwd)
        
        pwdEntry.pack(side="left",padx=3)
        ttk.Button(temp,text="Copy", width=5,command=lambda:self.__clipButton(self.__elementPassword.get())).pack(side="right",padx=3)

        ttk.Label(self,textvariable=self.__elementComment,width=60,anchor="center").pack(pady=5)
        
        


        temp = ttk.Frame(self)
        temp.pack(fill="x",pady=25)

        def next():
            self.master.position += 1
            self.updateElement()

        def previous():
            self.master.position -= 1
            self.updateElement()

        self.__nextButton = ttk.Button(temp, text="Next",command=next)
        self.__previousButton = ttk.Button(temp, text="Previous",command=previous)


    def updateElement(self):
        self.__elementName.set(self.master.getName())
        self.__elementUser.set(self.master.getUser())
        self.__elementPassword.set(self.master.getPassword())
        self.__elementComment.set(self.master.getComment())
        self.__nextButton.pack_forget()
        self.__previousButton.pack_forget()
        if len(self.master.elementsSelected) == 1:
            return None
        elif self.master.position == 0:
            self.__nextButton.pack(side="right")
        elif self.master.position == len(self.master.elementsSelected)-1:
            self.__previousButton.pack(side="left")
        else :
            self.__nextButton.pack(side="right")
            self.__previousButton.pack(side="left")

    def __clipButton(self,text:str):
        self.clipboard_clear()
        self.clipboard_append(text)

    def customPack(self):
        self.pack()

    def resetEntry(self):
        self.__elementName.set("")
        self.__elementUser.set("")
        self.__elementPassword.set("")
        self.__elementComment.set("")
