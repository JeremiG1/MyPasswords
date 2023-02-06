from tkinter import ttk

class EditElementFrame(ttk.Frame):
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
        self.__passwordEntry = ttk.Entry(temp,width=50)
        self.__passwordEntry["show"] = "*"
        self.__passwordEntry.pack(side="left", padx=3)

        
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

     
        self.__addElementButton = ttk.Button(self, text="Edit",command=self.__editElement)
        self.__addElementButton.pack(padx=5,pady=5)

        self.__messageLabel = ttk.Label(self)
        self.__messageLabel.pack(pady=3)


    def __editElement(self):
        if (self.__nameEntry.get() == "" or
            self.__userEntry.get() == "" or
            self.__passwordEntry.get() == "" or
            self.__ConfirmeEntry.get() == ""):
            self.__messageLabel.config(text="Invalide input",foreground="red")
        elif (self.__passwordEntry.get() != self.__ConfirmeEntry.get()):
            self.__messageLabel.config(text="Password error",foreground="red")
        else:
            self.__messageLabel.config(text="Element successfully added",foreground="green")
            self.master.editCommand(self.__nameEntry.get(), self.__userEntry.get(), self.__passwordEntry.get(), self.__CommentEntry.get())
            self.resetEntry()


    def updateParam(self):
        self.__nameEntry.insert("end", self.master.getName())
        self.__userEntry.insert("end", self.master.getUser())
        self.__passwordEntry.insert("end", self.master.getPassword())
        self.__ConfirmeEntry.insert(0,self.__passwordEntry.get())
        self.__CommentEntry.insert("end", self.master.getComment())
    
    def customPack(self):
        self.pack()

    def resetEntry(self):
        self.__nameEntry.delete(0,"end")
        self.__userEntry.delete(0,"end")
        self.__passwordEntry.delete(0,"end")
        self.__ConfirmeEntry.delete(0,"end")
        self.__messageLabel.config(text="")
        self.__CommentEntry.delete(0,"end")