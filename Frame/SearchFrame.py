from tkinter import ttk
import tkinter as tk

class SearchFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.__elements = []
        self.__offset = 0
        


        self.__search = ttk.Entry(self)
        self.__search.bind("<KeyRelease>",self.__updateListBoxEvent)
        self.__search.pack(pady=5)
        self.__listBox = tk.Listbox(self)   
        self.__listBox.bind('<<ListboxSelect>>',self.__selectElementEvent)
        self.__listBox.bind('<Motion>',self.__hover)
        self.__listBox.bind("<MouseWheel>",self.__setOffset)
        self.__listBox.bind("<Leave>", self.__resetColor)
        self.__listBox.pack(fill="both")
        ttk.Button(self, text="Add Element",command=self.master.packAddElementBody).pack(pady=5)

    def __hover(self,event:tk.Event):
        self.__resetColor()   
        index = int((event.y/self.__listBox.winfo_height()) * 10)
        self.__listBox.itemconfigure(index+self.__offset,bg="#007fff")
    
    def __resetColor(self,event=None):
        for x in range(self.__listBox.size()):
            self.__listBox.itemconfigure(x,bg="#333333")

    def __setOffset(self,event:tk.Tk):
        if event.delta < 0 :
            if (self.__listBox.size() - self.__offset - 4) <= 10:
                self.__offset = self.__listBox.size() - 10
            else:
                self.__offset += 4
        elif event.delta > 0 and self.__offset > 0:
            if self.__offset < 4:
                self.__offset = 0
            else:
                self.__offset -= 4
        self.__hover(event)
 

    def __updateListBoxEvent(self,event:tk.Event):
        if event.keysym == "Return":
            elementName = self.__search.get()
            for element in self.__elements:
                if elementName == element["name"]:
                    self.selectElement(elementName)
                    return None
        else:
            self.__updateListBox(filter=self.__search.get())

    def __updateListBox(self,filter:str = None):
        self.__listBox.delete(0,"end")
        present = []
        for element in self.__elements:
            if element["name"] in present:
                continue
            if (filter is None):
                self.__listBox.insert("end",element["name"])
                present.append(element["name"])
            else:
                if element["name"].find(filter) != -1:
                    self.__listBox.insert("end",element["name"])
                    present.append(element["name"])

    def selectElement(self, name:str, position:int = 0):
        self.master.position = position
        selectedElements = [x for x in self.__elements if x["name"] == name]
        if len(selectedElements) == 0:
            self.master.packSearchBody()
            self.master.elementsSelected = []
        else:
            self.master.elementsSelected = selectedElements
            self.master.packElementBody()

    def __selectElementEvent(self,event:tk.Event):
        index = event.widget.curselection()
        if index == ():
            return None
        name = event.widget.get(index)
        self.selectElement(name)

    def setElements(self,elements:list):
        self.__elements = elements

    def customPack(self):
        self.pack(pady=10)

    def resetEntry(self):
        self.__search.delete(0,"end")
        self.__updateListBox()
    
    def updateParam(self):
        self.__updateListBox()