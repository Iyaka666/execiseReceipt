#SIN ENCAPSULACION
#quita caracteristicas importantes del polimorfismo en Python (averiguar)

def show2Column(array1 = (), array2 = ()):
    #the function show  the information of classes, Home, Suscriber and Receipt, it used in the method description.
    table = ''
    if len(array1) == len(array2):
        i = 0
        while i < len(array1):
            table += array1[i] + ": " + array2[i] + "\n"
            if i == (len(array1) - 1):
                table += array1[i] + ": " + array2[i]
            i += 1
    return table

def validateString(messageInput = ' '):
    s = ' '
    while not s.isalpha():
            s = ((input(messageInput + " --> ")).strip()).lower()
            if s.isalpha() == False:
                print("Solo ingrese letras, por favor")
    return s

def validateAddress(messageInput = "Ingrese la dirección", ):
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

def validateDigitAndNumberZRange(quantityFinalDigit , quantityInitialDigit = 0, messageInput = "Ingrese el número"):
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


def validateDigitAndNumberZ(quantityDigits, messageInput = "Ingrese el número"):
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