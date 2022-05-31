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