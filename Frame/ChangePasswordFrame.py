from tkinter import ttk

class ChangePasswordFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

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

     
        ttk.Button(self, text="Change password",command=self.__changePassword).pack(padx=5,pady=5)
        

        self.__messageLabel = ttk.Label(self)
        self.__messageLabel.pack(pady=3)

    def __changePassword(self):

        if (self.__passwordEntry.get() == ""):
            self.__messageLabel.config(text="Invalide input",foreground="red")
        elif (self.__passwordEntry.get() != self.__ConfirmeEntry.get()):
            self.__messageLabel.config(text="Password invalid",foreground="red")
        else:
            self.master.changeLoginPwd(self.__passwordEntry.get())
            self.master.packSearchBody()


    def customPack(self):
        self.pack()
    
    def resetEntry(self):
        self.__passwordEntry.delete(0,"end")
        self.__ConfirmeEntry.delete(0,"end")
        self.__messageLabel.config(text="")