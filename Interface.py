import tkinter as tk
from tkinter import ttk
import crypto
from Frame import *
import os
import file


class Interface(ttk.Frame):
    def __init__(self, master:tk.Tk) -> None:
        super().__init__(master)
        self.pack(fill="both", padx=5, pady=5, expand=True)
        self.master = master
        self.__key1 = None
        self.__key2 = None
        self.position = 0
        self.elementsSelected = []
    
    
        header = ttk.Frame(self)
        header.pack(fill="x")
        

        self.__loginBody = LoggingFrame(self)
        self.__changePasswordBody = ChangePasswordFrame(self)
        self.__firstConnectionBody = FirstConnectionFrame(self)
        self.__searchBody = SearchFrame(self)
        self.__elementBody = ElementFrame(self)
        self.__addElementBody = AddElementFrame(self)
        self.__editElementBody = EditElementFrame(self)



        self.__searchHeader = ttk.Frame(header)
        self.__searchHeader.pack(fill="x")
        ttk.Button(self.__searchHeader, text="Logout",command=self.packLoginBody).pack(side="right",padx=3)
        ttk.Button(self.__searchHeader, text="Change pwd",command=self.packChangePasswordBody).pack(side="left",padx=3)

        self.__elementHeader = ttk.Frame(header)
        ttk.Button(self.__elementHeader, text="Back",command=self.packSearchBody).pack(side="left",padx=3)
        ttk.Button(self.__elementHeader, text="Edit",command=self.packEditElementBody).pack(side="right",padx=3)

        self.__addElementHeader = ttk.Frame(header)
        ttk.Button(self.__addElementHeader, text="Back",command=self.packSearchBody).pack(side="left",padx=3)

        self.__EditHeader = ttk.Frame(header)
        ttk.Button(self.__EditHeader, text="Cancel",command=self.packElementBody).pack(side="left",padx=3)
        ttk.Button(self.__EditHeader, text="Remove",command=self.__removeButton).pack(side="right",padx=3)

        self.__changePasswordHeader = ttk.Frame(header)
        ttk.Button(self.__changePasswordHeader, text="Cancel",command=self.packSearchBody).pack(side="left",padx=3)

        if (crypto.verifFirstConnection()):
            self.packFirstConnectionBody()
        else:
            self.packLoginBody()



    ################################
    #addElement function
    ################################

    def editCommand(self,name:str,user:str,password:str,comment:str):
        dic = {"name":self.elementsSelected[self.position]["name"],
               "user":self.elementsSelected[self.position]["user"],
               "password":self.elementsSelected[self.position]["password"],
               "comment":self.elementsSelected[self.position]["comment"]}
        crypto.removeElement(dic,self.__key2)
    
        self.addElementToDb(name,user,password,comment)
        self.__searchBody.updateParam()
        if name != self.elementsSelected[self.position]["name"]:
            self.__searchBody.selectElement(name)
        else:
            self.__searchBody.selectElement(name,len(self.elementsSelected)-1)

    def __removeButton(self):
        crypto.removeElement(self.elementsSelected[self.position],self.__key2)
        self.__updateSelectedElements(self.elementsSelected[self.position]["name"])
        
    def __updateSelectedElements(self, name:str = None):
        self.__updateElements()
        self.__searchBody.updateParam()
        self.__searchBody.selectElement(name)

    def addElementToDb(self,name:str,user:str,password:str,comment:str):
        dic = {"name":name, "user": crypto.encrypt(user,self.__key1).decode("utf-8"), "password":crypto.encrypt(password,self.__key1).decode("utf-8"), "comment":crypto.encrypt(comment,self.__key1).decode("utf-8")}
        crypto.newElement(dic,self.__key2)
        self.__updateElements()
        self.__searchBody.updateParam()

    def login(self, pwd:str):
        self.__key1, self.__key2 = crypto.verifPwd(pwd)
        if (self.__key1 is not None):
            self.__updateElements()
            self.__searchBody.updateParam()
            self.packSearchBody()
            return True
        else:
            return False

    def changeLoginPwd(self,password:str):
        self.__key1, self.__key2 = crypto.changePwd(self.__key1, self.__key2, password)
        self.__updateElements()
        

    ################################
    #pack
    ################################
    def __unpackAll(self):
        self.__unpackBody()
        self.__unpackHeader()
        self.__clear()

    def __clear(self):
        self.__searchBody.resetEntry()
        self.__addElementBody.resetEntry()
        self.__loginBody.resetEntry()
        self.__elementBody.resetEntry()
        self.__editElementBody.resetEntry()
        self.__changePasswordBody.resetEntry()
        self.__firstConnectionBody.resetEntry()

    def __unpackBody(self):
        self.__addElementBody.pack_forget()
        self.__searchBody.pack_forget()
        self.__elementBody.pack_forget()
        self.__editElementBody.pack_forget()
        self.__loginBody.pack_forget()
        self.__changePasswordBody.pack_forget()
        self.__firstConnectionBody.pack_forget()

    def __unpackHeader(self):
        self.__searchHeader.pack_forget()
        self.__elementHeader.pack_forget()
        self.__addElementHeader.pack_forget()
        self.__EditHeader.pack_forget()
        self.__changePasswordHeader.pack_forget()

    def packLoginBody(self):
        self.__unpackAll()
        self.__resetKeys()
        self.__loginBody.customPack()
    
    def packSearchBody(self):
        self.__unpackAll()
        self.__searchHeader.pack(fill="x")
        self.__searchBody.customPack()

    def packElementBody(self):
        self.__unpackAll()
        self.__elementHeader.pack(fill="x")
        self.__elementBody.customPack()
        self.__elementBody.updateElement()

    def packAddElementBody(self):
        self.__unpackAll()
        self.__addElementHeader.pack(fill="x")
        self.__addElementBody.customPack()

    def packEditElementBody(self):
        self.__unpackAll()
        self.__EditHeader.pack(fill="x")
        self.__editElementBody.customPack()
        self.__editElementBody.updateParam()

    def packFirstConnectionBody(self):
        self.__unpackAll()
        self.__firstConnectionBody.customPack()

    def packChangePasswordBody(self):
        self.__unpackAll()
        self.__changePasswordHeader.pack(fill="x")
        self.__changePasswordBody.customPack()

    
    
    ################################
    #loged
    ################################

    
    def __resetKeys(self):
        self.__key1 = None
        self.__key2 = None

    def __updateElements(self):
        self.__searchBody.setElements(crypto.getElement(self.__key2))



    ################################
    #login function
    ################################

    def getName(self):
        return self.elementsSelected[self.position]["name"]

    def getUser(self):
        return crypto.decrypt(self.elementsSelected[self.position]["user"],self.__key1).decode("utf-8")
    
    def getPassword(self):
        return crypto.decrypt(self.elementsSelected[self.position]["password"],self.__key1).decode("utf-8")

    def getComment(self):
        return crypto.decrypt(self.elementsSelected[self.position]["comment"],self.__key1).decode("utf-8")



if __name__ == "__main__":
    root = tk.Tk()
    Interface(root)

    icon = tk.PhotoImage(data=file.ICON)
    root.iconphoto(True,icon)
    root.wm_geometry("600x320")
    root.title("MyPasswords")
    
    root.tk.call("source",os.path.join(crypto.PATH,"azure.tcl"))
    root.tk.call("set_theme", "dark")
    root.resizable(0,0)
    root.mainloop()