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
      self.__medico = ""
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
    def verMedico(self): #nuevo atributo
        return self.__medico
    
    #Setters
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarMedico(self,m):
        self.__medico = m
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

class Sistema:
    def __init__(self):
        self.__paciente = {}
        self.inventario = []  
        
    def agregarPacientes(self, paciente):
        self.__pacientes[paciente.verCedula()] = paciente
        print("----------------------------------------------------------")
        print(f"Paciente {paciente.verNombre()} registrado correctamente.")
        print("----------------------------------------------------------")

    def asignarImplanteAPaciente(self, cedula, implante, fecha_implantacion, medico_responsable, estado_implante):
        paciente = self.__pacientes.get(cedula)
        if paciente:
            implante.asignarFecha(fecha_implantacion)
            implante.asignarEstado(estado_implante)
            implante.asignarMedico(medico_responsable)# Agregar información adicional si es necesario, como el médico responsable
            paciente.asignarImplante(implante)
            print("----------------------------------------------------------")
            print(f"Implante asignado a {paciente.verNombre()} correctamente.")
            print("----------------------------------------------------------")
            
        else:
            print("---------------------------------------------------")
            print(f"No se encontró un paciente con la cédula {cedula}.")
            print("---------------------------------------------------")
            
    def realizarSeguimientoImplante(self, id_implante, fecha_revision, estado_implante):
        for implante in self.__implantes:
            if implante.verId() == id_implante:
                # Actualizar información de seguimiento del implante
                implante.asignarEstado(estado_implante)
                implante.asignarFecha(fecha_revision) # Registrar la fecha de revisión
                # Agregar cualquier otra información de seguimiento si es necesario
                print("-------------------------------------------------------------")
                print(f"Seguimiento realizado para el implante con ID {id_implante}.")
                print("-------------------------------------------------------------")
                return
        print("-------------------------------------------------")
        print(f"No se encontró un implante con ID {id_implante}.")
        print("-------------------------------------------------")
        
    def obtenerPaciente(self, cc):
        return self.__paciente.get(cc)

    def agregar_implante(self):
        tipo_implante = valid_letter("""Ingrese el tipo de implante:
                                     a. Protesis_C
                                     b. Marcapasos
                                     c. Stents
                                     d. ImplantesD
                                     e. Protesis_R
                                     >>> """)

        if tipo_implante == "a":
            implante = Protesis_C()
        
        elif tipo_implante == "b":
            implante = Marcapasos()
            
        elif tipo_implante == "c":
            implante = Stents()
           
        elif tipo_implante == "d":
            implante = ImplantesD()
            
        elif tipo_implante == "e":
            implante = Protesis_R()
            
        else:
            print("---------------------------")
            print("Tipo de implante no válido.")
            print("---------------------------")
            return
    
        implante.asignarNombre(valid_letter("Ingrese el nombre del implante: "))
        implante.asignarId(valid_int("Ingrese el ID del implante: "))
        implante.asignarEstado(valid_letter("INgresar estado del implante: "))
        implante.asignarFecha(valid_date)
        implante.asignarFabricante(valid_letter("Ingresar fabricante: "))
        self.inventario.append(implante)
        print("--------------------------------")
        print("Implante agregado correctamente.")
        print("--------------------------------")

    def eliminar_implante(self):
        id_implante = valid_int("Ingrese el ID del implante que desea eliminar: ")

        # Busca el implante en el inventario de la instancia de la clase
        for i, implante in enumerate(self.inventario):
            if implante.verId() == id_implante:
                del self.inventario[i]
                print("-------------------------------------------------------")
                print(f"Implante con ID {id_implante} eliminado correctamente.")
                print("-------------------------------------------------------")
                return

        print("------------------------------------------------------------------")
        print(f"No se encontró un implante con ID {id_implante} en el inventario.")
        print("------------------------------------------------------------------")

    def editar_implante(self):
        id_implante = valid_int("Ingrese el ID del implante que desea editar: ")

        # Busca el implante en el inventario de la instancia de la clase
        for i, implante in enumerate(self.inventario):
            if implante.verId() == id_implante:
                # Edita los detalles del implante
                print("-----------------------------------------------------")
                print(f"Implante con ID {id_implante} editado correctamente.")
                print("-----------------------------------------------------")
                return

        print("------------------------------------------------------------------")
        print(f"No se encontró un implante con ID {id_implante} en el inventario.")
        print("------------------------------------------------------------------")

    def visualizar_inventario(self):
        print("\nInventario de Implantes:")
        for implante in self.inventario:
            print(f"Nombre: {implante.verNombre()}")
            print(f"\nTipo: {type(implante).__name__}")
            print(f"ID: {implante.verId()}")
            print(f"Fecha: {implante.verFecha()}")
            print(f"Estado: {implante.verEstado()}")
            print(f"Fabricante: {implante.verFabricante()}")
            
def main():
    sis = Sistema()

    while True:
        print("""\n1. Agregar Implante y asignarlo a un paciente
            2. Eliminar Implante
            3. Editar Información de Implante
            4. Visualizar Inventario
            5. Agregar paciente
            6. Obtener paciente
            7. Seguimiento de implantes
            8. Salir""")

        opcion = valid_int("Seleccione una opción (1-5): ")

        if opcion == 1:
            #agregar implante y asignar a paciente
            tipo_implante = valid_letter("Ingrese el tipo de implante (Protesis_C, Marcapasos, Stents, ImplantesD, Protesis_R): ")
            implante = None
            # Crear instancia de tipo de implante según la opción ingresada
            # Solicitar detalles específicos del implante
            # Solicitar información sobre el paciente al que se asignará el implante
            cedula_paciente = valid_int("Ingrese la cédula del paciente al que se asignará el implante: ")
            fecha_implantacion = valid_date("Ingrese la fecha de implantación: ")
            medico_responsable = valid_letter("Ingrese el médico responsable: ")
            estado_implante = valid_letter("Ingrese el estado del implante: ")

            sis.asignarImplanteAPaciente(cedula_paciente, implante, fecha_implantacion, medico_responsable, estado_implante)
        
        elif opcion == 2:
            sis.eliminar_implante()
        elif opcion == 3:
            sis.editar_implante()
        elif opcion == 4:
            sis.visualizar_inventario()
            
        elif opcion == 5:
            #agregar paciente 
            paciente = Paciente()
            # Solicitar detalles del paciente
            sis.agregarPaciente(paciente)
            
        elif opcion == 6:
            sis.obtenerPaciente()
            
        elif opcion == 7:
            #seguimiento de implantes
            id_implante = valid_int("Ingrese el ID del implante para realizar seguimiento: ")
            fecha_revision = valid_date("Ingrese la fecha de revisión: ")
            estado_implante = valid_letter("Ingrese el nuevo estado del implante: ")

            sis.realizarSeguimientoImplante(id_implante, fecha_revision, estado_implante)
            
        elif opcion == 8:
            print("-------------")
            print("¡Hasta luego!")
            print("-------------")
            break
        
        else:
            print("-----------------------------------")
            print("Opción no válida. Intente de nuevo.")
            print("-----------------------------------")
            
if __name__ == "__main__":
    main()
