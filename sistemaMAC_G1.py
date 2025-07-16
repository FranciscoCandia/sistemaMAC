# Menú principal
def menu():

    while True:
        print(" =============================================")
        print("     Bienvenido al sistema - VALIDA - MAC     ")
        print(" =============================================") 
        print("1. Registrar Ciudadano")
        print("2. Buscar ciudadano por DNI")
        print("3. Ver todos los ciudadanos registrados")
        print("4. Ver historial de un ciudadano")
        print("5. Salir")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            dni = input("Ingrese DNI del ciudadano: ")

        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")
