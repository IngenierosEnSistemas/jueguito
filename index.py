continuar = input("Desea iniciar el juego? ")
while continuar == "Yes" or continuar == "yes" or continuar == "si" or continuar == "Si":
    a = int(input("Ingrese in numero del 1 al 10 :): "))

    if a == 1:
        print("Porque un numero tan bajo?")
    elif a == 2:
        print("El numero 2 de la seleccion argentina lo tiene Juan Foyth")
    elif a == 3:
        print("No me gusta el numero 3")
    elif a == 4:
        print("Es la calificación que la mayoria del curso anhela")
    elif a == 5:
        print("Llegaré a quinto de la ingenieria sin recursar ninguna materia?")
    elif a == 6:
        print("Simplemente Germán Pezzella")
    elif a == 7:
        print("BIENNNNNNN, promocionaste")
    elif a == 8:
        print("El culo te abrocho")
    elif a == 9:
        print("Para poner 9 mejor pone  10")
    elif a == 10:
        print("Gracias por el 10 de calificacion, prometo disfrutarlo :)")
    else:
        print("Te dije que del 1 al 10")
    print("Desea hacerlo denuevo?")
    continuar = string (input())
