

print("¡Hola! Este es un convertidor de unidades que convierte los kilómetros en millas")


while True:


    print("Por favor, ingrese una cantidad de kilómetros que le gustaría convertir en millas. ¡Ingrese solo un número!")



    km = float(km.replace(",", "."))   # reemplaza la coma con un punto, si el usuario ingresó una coma


    miles = km * 0.621371

    print("{0} kilómetros is {1} millas.".format(km, miles))

    choice = input("¿Te gustaría hacer otra conversión (y / n):? ")

    if choice.lower() != "y" and choice.lower() != "si":


        break