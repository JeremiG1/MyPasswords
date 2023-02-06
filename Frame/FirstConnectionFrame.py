from tkinter import ttk
import crypto


class FirstConnectionFrame(ttk.Frame):
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

     
        ttk.Button(self, text="Register",command=self.__registerPassword).pack(padx=5,pady=5)
        

        self.__messageLabel = ttk.Label(self)
        self.__messageLabel.pack(pady=3)

    def __registerPassword(self):
        if (self.__passwordEntry.get() == ""):
            self.__messageLabel.config(text="Invalide input",foreground="red")
        elif (self.__passwordEntry.get() != self.__ConfirmeEntry.get()):
            self.__messageLabel.config(text="Password invalid",foreground="red")
        else:
            crypto.savePW(self.__passwordEntry.get())
            crypto.resetData()
            self.master.packLoginBody()


    def customPack(self):
        self.pack()
    
    def resetEntry(self):
        self.__passwordEntry.delete(0,"end")
        self.__ConfirmeEntry.delete(0,"end")
        self.__messageLabel.config(text="")