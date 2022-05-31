from Home import Home

from Suscriber import *

class Receipt():
    #Constants
    VALUE_KW = 250
    VALUE_PUBLIC_LIGHTING = 90
    PERCENTAGE_IVA = 0.08
    DISCOUNT_1_AND_2 = 0.45
    DISCOUNT_3 = 0.2
    INCREASE_4_AND_5 = 0.15
    INCREASE_6_AND_7 = 0.4
    
    def __init__(self, readBefore = 0, readAfter = 0, homeUser = Home(), subscribeUser = Subscriber()):
        self.readBefore = readBefore
        self.readAfter = readAfter
        self.homeUser = homeUser
        self.subscriber = subscribeUser
    
    def getReadBefore(self): return self.readBefore
    
    def setReadBefore(self, inT): self.readBefore = inT
    
    def getReadAfter(self): return self.readAfter
    
    def setReadAfter(self, inT): self.readAfter = inT
    
    def getHomeUser(self): return self.homeUser
    
    def getSuscribeUser(self): return self.getSuscribeUser
    
    def consumption(self): return self.readBefore - self.readAfter
    
    
    def positionBasic(self):
        if self.homeUser.getStratum() >= 1 and self.homeUser.getStratum() <= 2:
            return 2000
        elif self.homeUser.getStratum() == 3:
            return 5000
        elif self.homeUser.getStratum() >= 4 and self.homeUser.getStratum() <= 5:
            return 8000
        elif self.homeUser.getStratum() >= 6 and self.homeUser.getStratum() <= 7:
            return 12000
    
    def valueConsumption(self):
        return self.consumption() * self.VALUE_KW
    
    def valuePublicLighting(self):
        return self.consumption() * self.VALUE_PUBLIC_LIGHTING
    
    def valueDiscount(self):
        if self.homeUser.getStratum() >= 1 and self.homeUser.getStratum() <= 2: 
            return self.valueConsumption() * self.DISCOUNT_1_AND_2
        elif self.homeUser.getStratum() == 3:
            return self.valueConsumption() * self.DISCOUNT_3
        else: 
            return 0
    
    def valueIncrease(self):
        if self.homeUser.getStratum() >= 4 and self.homeUser.getStratum() <= 5:
            return self.valueConsumption() * self.INCREASE_4_AND_5
        elif self.homeUser.getStratum() >= 6 and self.homeUser.getStratum() <= 7:
            return self.valueConsumption() * self.INCREASE_6_AND_7
        else:
            return 0
    
    def valueIVA(self):
        return (self.valueConsumption() * self.PERCENTAGE_IVA) + (self.valuePublicLighting() * self.PERCENTAGE_IVA)
    
    def total(self):
        return self.valueConsumption() + self.valuePublicLighting() + self.valueDiscount() + self.valueIncrease() + self.valueIVA()
    
    def description(self):
        atribbs = ("Lectura actual de kW","Lectura del mes anterior")
        atribbsThisClass = (self.readAfter, self.readBefore)
        return show2Column(atribbs, atribbsThisClass)