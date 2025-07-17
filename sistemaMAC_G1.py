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
            print("=============================================")
            print("1. Registro Automático RENIEC")
            print("2. Capturar datos mediante escaneo (OCR)")
            print("=============================================")
            
            sub_opcion = input("Elija una opción: ")
            if sub_opcion == "1":
                sub_opcion = input("Ingrese DNI del. ciudadano: ")
                # Registrar ciudadano
                
            if sub_opcion == "2":
                print("=============================================")
                print(" Escaneando datos......")
                print(" Datos del ciudadano encontrado")
                print("=============================================")
                # Imprimir ciudadano
            
            break;
        
        elif opcion == "2":
            print("=======================================")
            sub_opcion = input(" Ingrese DNI del. ciudadano: ")
            # Buscar ciudadano
            
            print("=======================================")
            sub_opcion = input("0. Regresar: ")
            
        elif opcion == "3":
            print("================================")
            print(" Ciudadanos Registrados:")
            print("================================")
            # Listar ciudadanos
            
            print("================================")
            sub_opcion = input("0. Regresar: ")
            
        elif opcion == "4":
            print("=============================================")
            print("            Historial del ciudadano          ")
            print("=============================================")
            sub_opcion = input("Ingrese DNI del. ciudadano: ")
            # HIstorial ciudadano
            
            print("================================")
            sub_opcion = input("0. Regresar: ")
            
        elif opcion == "5":
            print("================================")
            print(" Saliendo del sistema. ¡Gracias!")
            print("================================")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.\n")

menu()

# Simulación de base de datos de RENIEC
RENIEC = {
    "12345678": {"nombres": "Carlos", "apellidos": "Sánchez", "direccion": "Av. Lima 123", "telefono": "999111222"},
    "87654321": {"nombres": "Lucía", "apellidos": "Ramírez", "direccion": "Jr. Arequipa 456", "telefono": "988222333"}
}

# Simulación de OCR desde documento escaneado
def ocr_simulado():
    return {
        "nombres": "NombreOCR",
        "apellidos": "ApellidoOCR",
        "direccion": "DireccionOCR",
        "telefono": "000000000"
    }

# Clase principal
class Ciudadano:
    def __init__(self, dni, nombres, apellidos, direccion, telefono):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_registro = datetime.datetime.now()

    def mostrar(self):
        return f"{self.nombres} {self.apellidos} - DNI: {self.dni}\nDirección: {self.direccion} - Tel: {self.telefono}"

