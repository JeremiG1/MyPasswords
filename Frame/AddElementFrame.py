from tkinter import ttk

class AddElementFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp,text="Name", width=12, anchor="e").pack(side="left")
        self.__nameEntry = ttk.Entry(temp,width=50)
        self.__nameEntry.pack()
        

        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp,text="User", width=12, anchor="e").pack(side="left")
        self.__userEntry = ttk.Entry(temp,width=50)
        self.__userEntry.pack(side="left", padx=3)


        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp,text="Password", width=12, anchor="e").pack(side="left")
        self.__pwdEntry = ttk.Entry(temp,width=50)
        self.__pwdEntry["show"] = "*"
        self.__pwdEntry.pack(side="left", padx=3)

        
        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp,text="Confirmation", width=12, anchor="e").pack(side="left")
        self.__ConfirmeEntry = ttk.Entry(temp,width=50)
        self.__ConfirmeEntry["show"] = "*"
        self.__ConfirmeEntry.pack(side="left", padx=3)

        temp = ttk.Frame(self)
        temp.pack(pady=5)
        ttk.Label(temp,text="Comment", width=12, anchor="e").pack(side="left")
        self.__CommentEntry = ttk.Entry(temp,width=50)
        self.__CommentEntry.pack(side="left", padx=3)

     
        ttk.Button(self, text="Add",command=self.__addElementToDb).pack(padx=5,pady=5)
        

        self.__messageLabel = ttk.Label(self)
        self.__messageLabel.pack(pady=3)

        
    def __addElementToDb(self):
        if (self.__nameEntry.get() == "" or
            self.__userEntry.get() == "" or
            self.__pwdEntry.get() == "" or
            self.__ConfirmeEntry.get() == ""):
            self.__messageLabel.config(text="Invalide input",foreground="red")
        elif (self.__pwdEntry.get() != self.__ConfirmeEntry.get()):
            self.__messageLabel.config(text="Password error",foreground="red")
        else:
            self.__messageLabel.config(text="Element successfully added",foreground="green")  
            self.master.addElementToDb(self.__nameEntry.get(),self.__userEntry.get(),self.__pwdEntry.get(),self.__CommentEntry.get())
            self.resetEntry()

    def customPack(self):
        self.pack()

    def resetEntry(self):
        self.__nameEntry.delete(0,"end")
        self.__userEntry.delete(0,"end")
        self.__pwdEntry.delete(0,"end")
        self.__ConfirmeEntry.delete(0,"end")
        self.__CommentEntry.delete(0,"end")
            