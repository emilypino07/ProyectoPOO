# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE PASAJERO

class Pasajero:
    """
    Clase que representa un pasajero dentro del sistema.
    Aplica encapsulamiento utilizando atributos privados,
    property y setter.
    """

    def __init__(self,
                 cedula: str,
                 nombre: str):
        #ATRIBUTOS PRIVADOS
        self.__cedula = cedula
        self.__nombre = nombre

    #ENCAPSULAMIENTOS
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        if nueva_cedula.strip() == "":
            raise ValueError("La cedula no puede estar vacia")
        if not nueva_cedula.isdigit() or len(nueva_cedula) != 10:
            raise ValueError("La cedula debe tener 10 digitos numericos")
        self.__cedula = nueva_cedula


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        if not nuevo_nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras")
        self.__nombre = nuevo_nombre

    #METODOS
    def mostrar_datos(self):

        print("\n--- PASAJERO ---")
        print(f"Cedula: {self.__cedula}")
        print(f"Nombre: {self.__nombre}")

    #STR
    def __str__(self):

        return (
            f"Cedula: {self.__cedula} | "
            f"Nombre: {self.__nombre}"
        )
