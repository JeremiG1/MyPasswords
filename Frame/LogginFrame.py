from tkinter import ttk


class LoggingFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
    
        self.__pwEntry = ttk.Entry(self)
        self.__emptyEntry()
        self.__pwEntry.bind("<FocusIn>", self.__handle_focus_in)
        self.__pwEntry.bind("<FocusOut>", self.__handle_focus_out)
        self.__pwEntry.bind("<KeyRelease>", self.__handle_enter)
        self.__pwEntry.pack(side="left",padx=5)
        ttk.Button(self, text="Login",command=self.__login).pack(side="left",padx=5)

    def __handle_focus_in(self, event):
        if (self.__pwEntry.get() == "Password" or self.__pwEntry.get() == "Wrong Password"):
            self.__pwEntry.delete(0, "end")
            self.__pwEntry.config(foreground ='white')
            self.__pwEntry["show"] = "*"

    def __handle_focus_out(self, event):
        if (self.__pwEntry.get() == '' ):
            self.__emptyEntry()
    

    def __handle_enter(self, event):
        if (event.keysym == "Return"):
            self.__login()

    def __login(self):
        if self.master.login(self.__pwEntry.get()):
            self.__emptyEntry()
        else:
            self.__wrongPwd()
        
    def __emptyEntry(self):
        self.__pwEntry.delete(0,"end")
        self.__pwEntry.insert(0,"Password")
        self.__pwEntry.config(foreground ='black')
        self.__pwEntry["show"] = ""

    def __wrongPwd(self):
        self.__pwEntry.delete(0,"end")
        self.__pwEntry.insert(0,"Wrong Password")
        self.__pwEntry.config(foreground ='red')
        self.__pwEntry["show"] = ""
        self.master.focus_set()

    def customPack(self):
        self.pack(pady=20, padx=5)

    def resetEntry(self):
        self.__emptyEntry()