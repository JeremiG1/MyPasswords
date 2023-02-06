import hashlib
import os
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import file

PATH = os.path.join(os.getenv("APPDATA"),"MyPasswords")



def generateFile():
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    if not os.path.exists(os.path.join(PATH, "db.txt")):
        with open(os.path.join(PATH, "db.txt"),"w"):
            pass
    if not os.path.exists(os.path.join(PATH, "privateKey.key")):
        with open(os.path.join(PATH, "privateKey.key"),"wb"):
            pass
    if not os.path.exists(os.path.join(PATH,"azure.tcl")):
        with open(os.path.join(PATH,"azure.tcl"),"wb") as f:
            f.write(file.AZURETCL)
    path = os.path.join(PATH,"theme")
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(os.path.join(path,"dark.tcl")):
        with open(os.path.join(path,"dark.tcl"),"wb") as f:
            f.write(file.DARKTCL)
    path = os.path.join(path,"dark")
    if not os.path.exists(path):
        os.makedirs(path)
        for key in file.IMAGE.keys():
            with open(os.path.join(path,key),"wb") as f:
                f.write(file.IMAGE[key])


def changePwd(oldKey1,oldKey2,newpwd:str):
    path = os.path.join(PATH, "db.txt")
    savePW(newpwd)
    newKey1, newKey2 = verifPwd(newpwd)
    oldList = getElement(oldKey2)
    newlist = []
    for elem in oldList:

        elem["user"] = encrypt(decrypt(elem["user"],oldKey1).decode("utf-8"),newKey1).decode("utf-8")
        elem["password"] = encrypt(decrypt(elem["password"],oldKey1).decode("utf-8"),newKey1).decode("utf-8")
        elem["comment"] = encrypt(decrypt(elem["comment"],oldKey1).decode("utf-8"),newKey1).decode("utf-8")
        newlist.append(encrypt(json.dumps(elem),newKey2).decode("utf-8") + "\n")
     
    with open(path,"w") as file:
        for line in newlist:
            file.write(line)
    return newKey1, newKey2

def verifFirstConnection():
    with open(os.path.join(PATH, "privateKey.key"),"rb") as file:
        if file.read() == b"":
            return True
    return False

def hash(message:str):
    m = hashlib.sha256()
    if type(message) == bytes:
        m.update(message)
    elif type(message) == str:
        m.update(message.encode("UTF-8"))
    else:
        raise ValueError("message type is invalid")
    return m.digest()

def savePW(pw:str):
    with open(os.path.join(PATH,"privateKey.key"), "wb+") as binary_file:
        binary_file.write(hash(hash(pw)))

def resetData():
    with open(os.path.join(PATH, "db.txt"), "w"):
        pass
        

def verifPwd(pw:str):
    with open(os.path.join(PATH,"privateKey.key"), "rb") as binary_file:
        validationKey =  binary_file.read()
        if (hash(hash(pw)) == validationKey):
            return hash(pw), hash(pw*2)
        return None,None

def encrypt(data:str, privateKey):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(privateKey, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))
    
def decrypt(data,privateKey):
    raw = b64decode(data)
    cipher = AES.new(privateKey, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)

def newElement(element:dict,key):
    path = os.path.join(PATH, "db.txt")
    data = json.dumps(element)
    with open(path,"a") as file:
        file.write(encrypt(data,key).decode("utf-8") + "\n")

def getElement(key):
    with open(os.path.join(PATH, "db.txt"), "r") as file:
        elements =  file.readlines()
        elements = [json.loads(decrypt(x.strip("\n").encode("utf-8"),key).decode("utf-8"))  for x in elements]
    elements.sort(key = lambda x: x["name"].lower())
    return elements

def removeElement(dic:dict,key):
    path = os.path.join(PATH, "db.txt")
    data = json.dumps(dic).encode("utf-8")
    with open(path,"r") as file:
        lines = file.readlines()
    with open(path,"w") as file:
        for line in lines:
            if decrypt(line.strip("\n").encode("utf-8"),key) != data:
                file.write(line)

generateFile()