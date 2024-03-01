def Calculadora_Credito():
    menu()
    seleccionMenu()


def menu():
    """Imprime en la terminal el menu del 1 al 5"""

    print ("1-Credito personal\n"
           "2-Credito vehicular\n"
           "3-Credito para vivienda\n"
           "4-Pymes\n"
           "5-Ayuda")

def espacioBlanco():
    """Hace un espacion el blanco en la terminal"""

    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


def seleccionMenu():
    """Con esta funcion por medio del teclado se 
    podra escoger a que opcion del menu se desea ingresar"""

    seleccion=int(input("Seleccione una opcion"))
    print()
    numeros=(1,2,3,4,5)
    while seleccion!= type(int) and seleccion not in numeros:
        print("ERROR\n"
              "La opcion selecionada debe de ser un numero entre 1 y 5\n")
        seleccion=int(input("Seleccione una opcion "))
        print()
    if seleccion==1:
        print("Credito personal")
    elif seleccion==2:
        print("Credito vehicular")
    elif seleccion==3:
        print("Credito para vivienda")
    elif seleccion==4: 
        print("Pymes")
    elif seleccion==5:
        print("Opciones de ayuda")

def montoCredito():
    """Funcion para que el usurario ingrese el monto que
    desea solicitar para el creddito."""
    credito=int(input("Ingrese el monto que desea solicitar para el credito "))
    return credito

def cuotasMensuales():
    """Toma el monto total del creddito y lo divide
    entre la canditad de meses en la que desea efectuar
    el pago"""

def montoFinal(prestamo, interes,meses):
    """Funcion que calcula el monto final del credtio"""
    return (prestamo*interes)/(1-(1+interes))**(-meses)





