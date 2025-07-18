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

    def getDNI(self):
        return self.__dni

    def mostrar(self):
        return f"{self.__nombres} {self.__apellidos} - DNI: {self.__dni} - Direccion: {self.__direccion} - Tel: {self.__telefono}"

    def __str__(self):
        return f"{self.__nombres} {self.__apellidos} - DNI: {self.__dni}\nDireccion: {self.__direccion} - Tel: {self.__telefono}"
      
class Validador:
    def validar_datos_personales(self, dni):
        while True:
            nombre = input("Nombres: ")
            if nombre.replace(" ", "").isalpha():
                break
            else:
                print("* Solo se permiten letras en el nombre.")

        while True:
            apellido = input("Apellidos: ")
            if apellido.replace(" ", "").isalpha():
                break
            else:
                print("* Solo se permiten letras en el apellido.")

        direccion = input("Direccion: ")

        while True:
            telefono = input("Telefono: ")
            if telefono.isdigit() and len(telefono) == 9:
                break
            else:
                print("* El telefono debe contener solo numeros y tener 9 digitos.")

        return Ciudadano(dni, nombre, apellido, direccion, telefono)

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

class CentroMAC:
    def __init__(self):
        self.__lista_ciudadanos = []

    def getListaciudadanos(self):
        return self.__lista_ciudadanos

    def RegistrarCiudadano(self, ciudadano):
        if self.Buscar(ciudadano.getDNI()) == None:
            self.__lista_ciudadanos.append(ciudadano)
            print('...Ciudadano Registrado Exitosamente...')
        else:
            print('Ya existe un ciudadano con ese DNI')

    def Buscar(self, dni):
        for c in self.__lista_ciudadanos:
            if c.getDNI() == dni:
                return c

        return None

    def Listar(self):
        for ciudadano in self.__lista_ciudadanos:
            print(ciudadano.mostrar())

    def MostrarHistorialCiudadano(self, dni):
        ciudadano = self.Buscar(dni)
        if ciudadano:
            ciudadano.mostrar_historial()
        else:
            print("Ciudadano no encontrado.")

# Simulacion de base de datos de RENIEC
RENIEC = {
    "12345678": {"nombres": "Carlos", "apellidos": "Sanchez", "direccion": "Av. Lima 123", "telefono": "999111222"},
    "87654321": {"nombres": "Lucia", "apellidos": "Ramirez", "direccion": "Jr. Arequipa 456", "telefono": "988222333"},
    "44332211": {"nombres": "Maria", "apellidos": "Fernandez Ruiz", "direccion": "Av. Brasil 321", "telefono": "976543210"},
    "55667788": {"nombres": "Pedro", "apellidos": "Quispe Huaman", "direccion": "Pasaje Union 100", "telefono": "965432187"}
}

# Simulacion de OCR desde documento escaneado
def ocr_simulado():
    return {
        "dni" : "70701010",
        "nombres": "Martin Alvarado",
        "apellidos": "Olivares Redema",
        "direccion": "Jr Alferez 784",
        "telefono": "974877121"
    }

# Menu principal
def menu():

    centroMAC = CentroMAC()

    while True:
        print("=============================================")
        print("    Bienvenido al sistema - VALIDA - MAC     ")
        print("=============================================")
        print("1. Registrar Ciudadano")
        print("2. Buscar ciudadano por DNI")
        print("3. Ver todos los ciudadanos registrados")
        print("4. Ver historial de un ciudadano")
        print("5. Salir")

        opcion = input("Elija una opcion: ")
        if opcion == "1":
            print("=============================================")
            print("1. Registro Automatico RENIEC")
            print("2. Capturar datos mediante escaneo (OCR)")
            print("=============================================")

            sub_opcion = input("Elija una opcion: ")
            if sub_opcion == "1":
                dni = input("Ingrese DNI del. ciudadano: ")
                datos = RENIEC.get(dni)
                if datos:
                    print("...Datos recogidos de RENIEC...")
                    ciudadano = Ciudadano(dni, datos["nombres"], datos["apellidos"], datos["direccion"], datos["telefono"])

                else:
                    print("...Datos no encontrados, por favor ingrese manualmente..")
                    # Validacion  de datos
                    valida = Validador()
                    ciudadano = valida.validar_datos_personales(dni)

                # Registro del ciudadano
                centroMAC.RegistrarCiudadano(ciudadano)
                print("========================================")
                back = input("s: Salir - m: Volver al menú ")
                if back == 's' or back == 'S':
                    break

            elif sub_opcion == "2":
                datos = ocr_simulado()
                print(" Datos del ciudadano encontrado:")
                print("=============================================")
                ciudadano = Ciudadano(datos["dni"], datos["nombres"], datos["apellidos"], datos["direccion"], datos["telefono"])
                print(ciudadano)

                register = input("\nDesea registrar al ciudadano (s/n): ")
                if register:
                    centroMAC.RegistrarCiudadano(ciudadano)
                    ciudadano.agregar_atencion(Reclamo("15/07/2025", "servicio de luz", "Resuelto"))
                    ciudadano.agregar_atencion(Solicitud("05/05/2025", "mantenimiento", "En proceso"))
                print("========================================")
                back = input("s: Salir - m: Volver al menu ")
                if back == 's' or back == 'S':
                    break

            else:
              print("Opcion no encontrada... volviendo al menu'\n")

        elif opcion == "2":
            print("=======================================")
            dni = input(" Ingrese DNI del ciudadano: ")
            print("=======================================")

            # Buscar ciudadano
            if centroMAC.Buscar(dni) == None:
                print(" Ciudadano no encontrado")
            else:
                print(centroMAC.Buscar(dni))

            print("=======================================")
            back = input("s: Salir - m: Volver al menu ")
            if back == 's' or back == 'S':
                break

        elif opcion == "3":
            if len(centroMAC.getListaciudadanos()) != 0:
                print("================================")
                print(" Ciudadanos Registrados:")
                print("================================")
                centroMAC.Listar()
            else:
                print("==================================")
                print("No existen ciudadanos registrados.")

            print("==================================")
            back = input("s: Salir - m: Volver al menu ")
            if back == 's' or back == 'S':
                break

        elif opcion == "4":
            dni = input("Ingrese DNI del ciudadano: ")
            # Historial ciudadano
            centroMAC.MostrarHistorialCiudadano(dni)

            print("================================")
            back = input("s: Salir - m: Volver al menu ")
            if back == 's' or back == 'S':
                break

        elif opcion == "5":
            print("================================")
            print(" Saliendo del sistema. ¡Gracias!")
            print("================================")
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.\n")
