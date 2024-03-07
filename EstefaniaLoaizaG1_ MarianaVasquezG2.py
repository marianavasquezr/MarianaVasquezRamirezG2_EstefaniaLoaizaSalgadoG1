#Se crea la clase padre implantes_M que es la de las caracteristicas generales de los implantes medicos
class Implantes_M():
    #Se  inicializa la clase con el metodo init
    def __init__(self):
        self.__nombre = ""
        self.__id = 0
        self.__fecha = ""
        self.__fabricante = ""
        self.__estado = ""
     
    #setters
    def asignarNombre(self, n):
        self.__nombre = n    
    def asignarId(self, id):
        self.__id = id    
    def asignarFecha(self, f):
        self.__fecha = f    
    def asignarFabricante(self, fa):
        self.__fabricante = fa    
    def asignarEstado(self, e):
        self.__estado = e
        
    #getters
    def verNombre(self):
        return self.__nombre
    def verId(self):
        return self.__id
    def verFecha(self):
        return self.__fecha
    def verFabricante(self):
        return self.__fabricante
    def verEstado(self):
        return self.__estado
        
class Protesis_C(Implantes_M):
    def __init__(self):
        Implantes_M.__init__(self)
        self.__material = ""
        self.__fijacion = ""
        self.__tamaño = 0.0
        
    #setters
    def asignarMaterial(self, m):
        self.__material = m    
    def asignarFijacion(self, fi):
        self.__fijacion = fi   
    def asignarTamaño(self, t): 
        self.__tamaño = t
            
    #getters
    def verMaterial(self):
        return self.__material
    def verFijacion(self):
        return self.__fijacion
    def verTamaño(self):
        return self.__tamaño
    
class Marcapasos(Implantes_M):
    def __init__(self):
        Implantes_M.__init__(self)
        self.__electrodos = 0
        self.__tipo = "" #alambrico o inalambrico
        self.__frecuencia = 0.0
        
    #setters
    def asignarElectrodos(self, el):
        self.__electrodos = el   
    def asignarTipo(self, ti):
        self.__tipo = ti   
    def asignarFrecuencia(self, fr): 
        self.__frecuencia = fr
            
    #getters
    def verElectrodos(self):
       return self.__electrodos    
    def verTipo(self):
       return self.__tipo
    def verFrecuencia(self):
       return self.__frecuencia
    
class Stents(Implantes_M):
    def __init__(self):
        Implantes_M.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
        self.__longitud = 0.0 # agrego atributos propios de la clase Stents y metodos
        self.__diametro = 0.0
        self.__material = ""

    #setters
    def asignarLongitud(self, l):
        self.__longitud = l
    def asignarDiametro(self, d):
        self.__diametro = d
    def asignarMaterial(self, m):
        self.__material = m

    #getters
    def verLongitud(self):
        return self.__longitud
    def verDiametro(self):
        return self.__diametro
    def verMaterial(self):
        return self.__material

class ImplantesD(Implantes_M):
    def __init__(self):
        Implantes_M.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
        self.__forma = ""
        self.__sistemaFijacion = ""
        self.__material = ""
    
    #setters
    def asignarForma(self, f):
        self.__forma = f
    def asignarSistemaFijacion(self, sist):
        self.__sistemaFijacion = sist
    def asignarMaterial(self, m):
        self.__material = m
    
    #getters
    def verForma(self):
        return self.__forma
    def verSistemaFijacion(self):
        return self.__sistemaFijacion
    def verMaterial(self):
        return self.__material

class Protesis_R(Implantes_M):
    def __init__(self):
        Implantes_M.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = 0.0
    
    #setters
    def asignarMateria(self, m):
        self.__material = m
    def asignarTipoFijacion(self, fij):
        self.__tipoFijacion = fij
    def asignarTamaño(self, t):
        self.__tamaño = t

    #getters
    def verMaterial(self):
        return self.__material 
    def verTipoFijacion(self):
        return self.__tipoFijacion
    def verTamaño(self):
        return self.__tamaño
class Sistema():
    pass