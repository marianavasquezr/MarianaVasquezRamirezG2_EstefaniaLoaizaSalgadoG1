#Se crea la clase padre implantes_M que es la de las caracteristicas generales de los implantes medicos
class Implantes_M():
    #Se  inicializa la clase con el metodo init
    def __init__(self):
        self.__nombre = ""
        self.__id = 0
        self.__fecha = ""
        self.__fabricante = ""
        self.__estado = ""
         
class Protesis_C(Implantes_M):
    pass

class Marcapasos(Implantes_M):
    pass

class Stents(Implantes_M):
    pass

class ImplantesD(Implantes_M):
    pass

class Protesis_R(Implantes_M):
    pass

class Sistema():
    pass