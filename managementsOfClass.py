from fuctions import *

from os import name as nameSystem

from os import system 

from Receipt import Receipt, Home, Subscriber

class InterfaceManagerClassesInConsole():
    def __init__(self, receipt = Receipt(), home = Home(), subscriber = Subscriber()):
        self.arrayObjects = [receipt, subscriber, home]
        self.option = 0 #This is to allow get in while the chooseOption()
        
        # For each the objects in arrayObjects has been created its validations with True or False
        # and added to conditionalObjects to show the information them  
        self.conditionalObjects = [False, False, False]
    
    def clearConsole(self):
        command = 'clear'
        if nameSystem in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            system(command)
    

    
    def chooseOption(self):
        while not self.option >= 1 and self.option <= 4:
            option1 = '1 <> {} datos del suscriptor'
            option2 = '2 <> {} datos de la vivienda del suscriptor'
            option3 = '3 <> {} las lecturas de Kilovatios'
            edit = [option1, option2, option3]
            i = 0
            while i < len(self.conditionalObjects):
                if self.conditionalObjects[i]:
                    edit[i].format('Mostrar')
                else:
                    edit[i].format("Ingresar")
            print("PROGRAMA RECIBO - TALLER IPOO".center())
            for j in edit:
                print(j)
            print("4 <> Terminar programa")
            self.option = int(input("--> "))
    
    def executionOption(self):
        if self.option == 1:
            self.arrayObjects[1].setNUIP(validateDigitAndNumberZRange(10,8,"Ingrese el N.U.I.P"))
            self.arrayObjects[1].setName(validateString("Ingrese el nombre"))
            self.arrayObjects[1].setLastName(validateString("Ingrese el apellido"))
            self.conditionalObjects[1] =  True
            self.clearConsole()            
        
        elif self.option == 2:
            self.arrayObjects[2].setStratum(validateString("Ingrese el estrato"))
            self.arrayObjects[2].setNeighbourhood(validateString("Ingrese el barrio"))
            self.arrayObjects[2].setCity(validateString("Ingrese la ciudad"))
            self.arrayObjects[2].setAddress(validateAddress())
            self.conditionalObjects[2] =  True
        
        elif self.option == 3:
            self.arrayObjects[0].setReadBefore(validateDigitAndNumberZRange(5,"Lectura del mes anterior --> "))
            self.arrayObjects[0].setReadAfter(validateDigitAndNumberZRange(5,"Lectura del mes actual --> "))
            self.conditionalObjects[0] =  True
        else:
            system('exit')
    
    def showData(self):
        j = 0
        for i in self.arrayObjects:
            if self.conditionalObjects[j]:
                print(i.description())
            j += 1
    
    def interfaceVisible(self, visible = False):
        while visible:
            self.showData()
            self.chooseOption()
            self.clearConsole()
            self.executionOption()