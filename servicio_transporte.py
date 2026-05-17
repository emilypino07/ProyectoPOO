# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE BASE: ServicioTransporte

from datetime import datetime
class ServicioTransporte:
    """
    Clase base que representa un servicio de transporte
    Aplica encapsulamiento utilizando atributos privados,
    property y setter para controlar el acceso a los datos.
    """
    def __init__(self, codigo:str,
                 nombre_pasajero: str,
                 fecha: str):
        #ATRIBUTOS PRIVADOS
        self.__codigo = codigo
        self.__nombre_pasajero = nombre_pasajero
        self.__fecha = fecha

    #ENCAPSULAMIENTOS
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):

        if nuevo_codigo.strip() == "":
            raise ValueError("El codigo no puede estar vacio")
        self.__codigo = nuevo_codigo

    #---------------------------------------------------------------------------
    @property
    def nombre_pasajero(self):
        return self.__nombre_pasajero

    @nombre_pasajero.setter
    def nombre_pasajero(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre_pasajero = nuevo_nombre

    #---------------------------------------------------------------------------
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        try:
            datetime.strptime(nueva_fecha, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Fecha invalida")
        self.__fecha = nueva_fecha


    # METODOS
    def calcular_tarifa(self):
        """
        Metodo que calcula la tarifa del servicio
        """
        return 0

    def mostrar_datos(self):
        pass

    #METODO STR
    def __str__(self):
        """
        Retorna informacion del objeto en texto
        """
        return (
            f"Codigo{self.__codigo}  |  "
            f"Pasajero: {self.__nombre_pasajero}  |  "
            f"Fecha: {self.__fecha}"
        )
