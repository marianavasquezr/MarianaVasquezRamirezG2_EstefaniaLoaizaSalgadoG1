#Funcion para validar enteros
from datetime import datetime,date
import re
r2 = r'^[A-Za-z-ñÑ-áÁéÉíÍóÓúÚ  ]+$'
patron = re.compile(r2)

def valid_date(msj):
    """Función para validar el ingreso de la fecha"""
    while True:
        print("---------------------------------------------------------------")
        print("A continuación ingrese la fecha en la que se realizó el estudio")
        print("Ingrese el día: ")
        dia = valid_int(msj)

        print("Ingrese el mes: ")
        mes = valid_int(msj)

        print("Ingresar el año: ")
        año = valid_int(msj)

        try:
            fecha = datetime(año, mes, dia)
            break
        except ValueError:
            print("-------------------------------------------")
            print("Fecha incorrecta, ingrese la fecha de nuevo")
            print("-------------------------------------------")

    print("Fecha: ", fecha.strftime("%d/%m/%Y"))
    return str(fecha)

def valid_float(msj):
    try:
        data = float(input(msj))
        return data
    except:
        print("----------------------------------------------------")
        print("Ingrese solo números decimales. Inténtelo nuevamente")
        print("----------------------------------------------------")
        return valid_float(msj)

def valid_int(value):
    ''' Funcion para validar números enteros '''
    while True:
        try:
            dato = int(input(value))
            return dato
        except ValueError:
            print("Ingrese un dato válido (números enteros)\n")
            
def valid_letter(question):
    import re
    ''' Valida que el dato ingresado sea de caracteres alfabetico, 
    incluyendo tildes, mayusculas, minusculas, espacio sin aceptar caracteres especiales o números '''
    while True:
        txt = input(question)
        try:
            if re.match("^[a-zA-Z-ñÑ-áÁéÉíÍóÓúÚ ]*$", txt):
                return txt
            else:
                print("Ingresó caracteres especiales o números")
        except ValueError:
            print("\nIngrese solo letras y espacios, intente de nuevo")
            
class Paciente:
    #Creamos el método constructor de Paciente para incializar sus atributos
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__implante = {} #contenedor para almacenar los implantes asociados al paciente
    
    #Getters  
    def verNombre(self):
        return self.__nombre
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    def verImplante(self):
        return self.__implante
    
    #Setters
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarImplante(self, implante):
        self.__implante[ImplantesM.verId] = implante 
        
    #Deleters
    def eliminarImplante(self, id):
        if id in self.__implante:
            del self.__implante[id]
            print(f"Implante con número de identificación {id} eliminado correctamente.")
        else:
            print(f"No se encontro un implante con número de identificación {id} asociado al paciente.")
            
#Se crea la clase padre implantes_M que es la de las caracteristicas generales de los implantes medicos
class ImplantesM():
    #Se  inicializa la clase con el metodo init
    def __init__(self):
        #Atributos privados
        self.__nombre = ""
        self.__id = 0
        self.__fecha = ""
        self.__fabricante = ""
        self.__estado = "" #activo o inactivo
    
    #Los setters y los getters son los metodos de acceso a los atributos
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
        
class Protesis_C(ImplantesM):
    def __init__(self):
        ImplantesM.__init__(self)
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
    
class Marcapasos(ImplantesM):
    def __init__(self):
        ImplantesM.__init__(self)
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
    
class Stents(ImplantesM):
    def __init__(self):
        ImplantesM.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
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

class ImplantesD(ImplantesM):
    def __init__(self):
        ImplantesM.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
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

class Protesis_R(ImplantesM):
    def __init__(self):
        ImplantesM.__init__(self) #llamo el inicializador de la clase implantes medicos y obtengo sus atributos
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
    def __init__(self):
        self.__paciente = {}

    def agregarPacientes(self, paciente):
        self.__paciente[paciente.verCedula] = paciente
    
    def obtenerPaciente(self, cc):
        return self.__paciente.get(cc)
