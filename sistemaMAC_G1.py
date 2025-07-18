import datetime
from abc import ABC, abstractmethod

# Clase principal
class Ciudadano:
    def __init__(self, dni, nombres, apellidos, direccion, telefono):
        self.__dni = dni
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_registro = datetime.datetime.now()
        self.__atenciones = []

    def agregar_atencion(self, atencion):
        self.__atenciones.append(atencion)

    def mostrar_historial(self):
        print("* =============================================== *")
        print("*               Historial de ciudadano            *")
        print("* =============================================== *")
        print(f"DNI: {self.__dni} \nNombre: {self.__nombres} {self.__apellidos}")
        for at in self.__atenciones:
            print(f"- {at.obtener_resumen()}")

    def mostrar(self):
        return f"{self.__nombres} {self.__apellidos} - DNI: {self.__dni} - Dirección: {self.__direccion} - Tel: {self.__telefono}"

class Atencion:
    def __init__(self, fecha, descripcion, estado):
        self._fecha = fecha
        self._descripcion = descripcion
        self._estado = estado

    @abstractmethod
    def obtener_resumen(self):
        pass

class Reclamo(Atencion):
    def obtener_resumen(self):
        return f"[{self._fecha}] Reclamo por {self._descripcion} - Estado: {self._estado}"

class Solicitud(Atencion):
    def obtener_resumen(self):
        return f"[{self._fecha}] Solicitud de {self._descripcion} - Estado: {self._estado}"

class Queja(Atencion):
    def obtener_resumen(self):
        return f"[{self._fecha}] Queja por {self._descripcion} - Estado: {self._estado}"


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
