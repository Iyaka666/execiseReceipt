from fuctions import *

class Home():
    
    def __init__(self, address = " ", neighbourhood = " ", city = " ", stratum = 0):
        self.address = address
        self.neighbourhood = neighbourhood
        self.city = city
        self.stratum = stratum
    
    def getAddress(self): return self.address
    
    def setAddress(self, strinG): self.address = strinG
    
    def getNeighbourhood(self): return self.neighbourhood
    
    def setNeighbourhood(self, strinG): self.neighbourhood = strinG
    
    def getCity(self): return self.city
    
    def setCity(self, strinG): self.city = strinG
    
    def getStratum(self): return self.stratum
    
    def setStratum(self, shortInt): self.stratum = shortInt
    
    def description(self):
        atribbs = ("Ciudad","Barrio","Estrato","Dirección")
        atribbsThisClass = (self.city, self.neighbourhood, self.stratum, self.address)
        return show2Column(atribbs, atribbsThisClass)