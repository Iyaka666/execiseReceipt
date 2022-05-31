from os import name as nameSystem

from os import system 

from Receipt import *

class InterfaceManagerClassesInConsole():
    def __init__(self, receipt = Receipt(), home = Home(), subscriber = Subscriber()):
        self.arrayObjects = [receipt, subscriber, home]
        self.option = 5 #This is to allow get in while the chooseOption()
        
        # For each the objects in arrayObjects has been created its validations with True or False
        # and added to conditionalObjects to show the information them  
        self.conditionalObjects = [False, False, False]
    
    def clearConsole(self):
        command = 'clear'
        if nameSystem in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            system(command)
    
    def validateString(self, messageInput = ' '):
        s = ' '
        while not s.isalpha():
                s = ((input(messageInput + " --> ")).strip()).lower()
                if s.isalpha() == False:
                    print("Solo ingrese letras, por favor")
        return s
    
    def validateAddress(self, messageInput = "Ingrese la dirección", ):
        s = ' '
        charactersToValidate = "#.-"
        s = input((messageInput.strip()).lower() + " --> ")
        listBool = []
        flagWhileMain = True
        flagWhile2 = False
        verifyLoop1 = 0
        while flagWhileMain:
            for i in s:
                if charactersToValidate.find(i) == -1: # search in the String if the characters to validate with its
                    listBool.append(False)
                else:
                    listBool.append(True)

            while verifyLoop1 < len(listBool):
                if listBool[verifyLoop1]:
                    flagWhileMain = False
                    break
                verifyLoop1 += 1
            
            if flagWhileMain == False:
                pass
            elif verifyLoop1 == len(listBool) + 1:
                    flagWhile2 = True

            while flagWhile2:
                print("has introducido un carácter que no pertenece a estos \nPor favor ingrese alguno de estos --> '#' , '.' , '-'")
                s = input(messageInput.strip() +" nuevamente"+ " --> ")
                break
        
        return s
    
    def validateDigitAndNumberZRange(self, quantityFinalDigit , quantityInitialDigit = 0, messageInput = "Ingrese el número"):
        nuip = ' ' #this value is the more important data for function is long number to validate 
        value = ' '
        keepWhile = True
        while keepWhile:
            nuip = input( (messageInput.strip()).lower() +" --> ")

            for i in messageInput.split(" "):
                if i == len(messageInput.split(" ")) - 1:
                    value = i.lower()

            while not (len(nuip) >= quantityInitialDigit and len(nuip) <= quantityFinalDigit) and (nuip.strip()).isdigit(): 
                error1 = f"La cantidad de digitos del {value} solo entre {quantityInitialDigit} a {quantityFinalDigit}, por favor"
                error2 = "Ingrese solo números entre 0 a 9, por favor"
                if (len(nuip) >= quantityInitialDigit and len(nuip) <= quantityFinalDigit) == False:
                    print(error1)
                    break
                elif (nuip.strip()).isdigit() == False:
                    print(error2)
                    break
                elif ((len(nuip) >= quantityInitialDigit and len(nuip) <= quantityFinalDigit) and (nuip.strip()).isdigit()) == False:
                    print(error1 + " además " + error2.lower())
                    break
                else:
                    keepWhile = False
                    break
        return int(nuip)
    
    
    def validateDigitAndNumberZ(self, quantityDigits, messageInput = "Ingrese el número"):
        nuip = value = ' '
        keepWhile = True
        while keepWhile:
            nuip = input( (messageInput.strip()).lower() +" --> ")

            for i in messageInput.split(" "):
                if i == len(messageInput.split(" ")) - 1:
                    value = i.lower()

            while not (len(nuip) == quantityDigits) and (nuip.strip()).isdigit(): 
                error1 = f"La cantidad de digitos del {value} debe ser {quantityDigits}, por favor"
                error2 = "Ingrese solo números entre 0 a 9, por favor"
                if (len(nuip) >= quantityDigits) == False:
                    print(error1)
                    break
                elif (nuip.strip()).isdigit() == False:
                    print(error2)
                    break
                elif ((len(nuip) >= quantityDigits) and (nuip.strip()).isdigit()) == False:
                    print(error1 + " además " + error2.lower())
                    break
                else:
                    keepWhile = False
                    break
        return int(nuip)
    
    def chooseOption(self):
        while not self.option >= 1 and self.option <= 4:
            conditions = [self.dataAdmittedSubscriber, self.dataAdmittedHome, self.dataAdmittedReceipt]
            option1 = '1 <> {} datos del suscriptor'
            option2 = '2 <> {} datos de la vivienda del suscriptor'
            option3 = '3 <> {} las lecturas de Kilovatios'
            edit = [option1, option2, option3]
            i = 0
            while i < len(conditions):
                if conditions[i]:
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
            self.arrayObjects[1].setNUIP(self.validateDigitAndNumberZRange(10,8,"Ingrese el N.U.I.P"))
            self.arrayObjects[1].setName(self.validateString("Ingrese el nombre"))
            self.arrayObjects[1].setLastName(self.validateString("Ingrese el apellido"))
            self.conditionalObjects[1] =  True
            self.clearConsole()            
        
        elif self.option == 2:
            self.arrayObjects[2].setStratum(self.validateString("Ingrese el estrato"))
            self.arrayObjects[2].setNeighbourhood(self.validateString("Ingrese el barrio"))
            self.arrayObjects[2].setCity(self.validateString("Ingrese la ciudad"))
            self.arrayObjects[2].setAddress(self.validateAddress())
            self.conditionalObjects[2] =  True
        
        elif self.option == 3:
            self.arrayObjects[0].setReadBefore(self.validateDigitAndNumberZRange(5,"Lectura del mes anterior --> "))
            self.arrayObjects[0].setReadAfter(self.validateDigitAndNumberZRange(5,"Lectura del mes actual --> "))
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
            #self.showData()
            self.chooseOption()
            self.clearConsole()
            self.executionOption()