from fuctions import *

class Subscriber():
    
    def __init__(self, nUIP = 0, name = " ", lastName = " "):
        self.nUIP = nUIP
        self.name = name
        self.lastName = lastName
    
    def getNUIP(self): return self.nUIP
    
    def setNUIP(self, lonG): self.nUIP = lonG
    
    def getName(self): return self.name
    
    def setName(self, strinG): self.name = strinG
    
    def getLastName(self): return self.lastName
    
    def setLastName(self, strinG): self.lastName = strinG
    
    def description(self):
        atribbs = ("Nombre", "Apellido", "Cédula")
        atribbsThisClass = (self.name, self.lastName, self.nUIP)
        return show2Column(atribbs, atribbsThisClass)