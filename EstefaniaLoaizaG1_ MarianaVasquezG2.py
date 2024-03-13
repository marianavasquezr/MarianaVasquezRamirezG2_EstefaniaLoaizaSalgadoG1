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
        self.__medico = ""
    
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
    def asignarMedico(self, m):
        self.__medico = m
        
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
    def verMedico(self):
        return self.__medico
        
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
        self.__paciente[paciente.verCedula()] = paciente
        
    def asignarImplanteAPaciente(self, cedula, implante, fecha_implantacion, medico_responsable, estado_implante):
        paciente = self.__paciente.get(cedula)
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
        for implante in self.inventario:
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
        
    def obtenerPaciente(self):
        print("\nOpciones de búsqueda:")
        print("1. Buscar por cédula")
        print("2. Buscar por nombre")
        print("3. Volver al menú principal")

        opcion = valid_int("Ingrese el número correspondiente a la opción de búsqueda: ")

        if opcion == 1:
            cedula = valid_int("Ingrese la cédula del paciente: ")
            paciente = self.__paciente.get(cedula)
            if paciente:
                self.mostrarDetallesPaciente(paciente)
            else:
                print("---------------------------------------------------")
                print(f"No se encontró un paciente con la cédula {cedula}.")
                print("---------------------------------------------------")
                
        elif opcion == 2:
            nombre = valid_letter("Ingrese el nombre del paciente: ")
            pacientes_encontrados = [paciente for paciente in self.__paciente.values() if paciente.verNombre().lower() == nombre.lower()]
            if pacientes_encontrados:
                print("\nPacientes encontrados:")
                for paciente in pacientes_encontrados:
                    self.mostrarDetallesPaciente(paciente)
                return pacientes_encontrados[0]
            else:
                print("-------------------------------------------------------")
                print(f"No se encontró ningún paciente con el nombre {nombre}.")
                print("-------------------------------------------------------")
                
        elif opcion == 3:
            return
        else:
            print("-----------------------------------")
            print("Opción no válida. Intente de nuevo.")
            print("-----------------------------------")

    def mostrarDetallesPaciente(self, paciente):
        print("\nDetalles del paciente:")
        print(f"Nombre: {paciente.verNombre()}")
        print(f"Cédula: {paciente.verCedula()}")
        print(f"Género: {paciente.verGenero()}")
        print(f"Médico Responsable: {paciente.verMedico()}")
        print("Implantes asociados:")
        for id_implante, implante in paciente.verImplante().items():
            print(f"ID: {id_implante}, Tipo: {type(implante).__name__}, Fecha de Implantación: {implante.verFecha()}, Estado: {implante.verEstado()}")


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
        implante.asignarEstado(valid_letter("Ingresar estado del implante: "))
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
                print("Implante encontrado. Detalles actuales:")
                print(f"Nombre: {implante.verNombre()}")
                print(f"Fecha: {implante.verFecha()}")
                print(f"Estado: {implante.verEstado()}")
                print(f"Fabricante: {implante.verFabricante()}")

                # Solicita la información actualizada
                while True:
                    print("\nOpciones de edición:")
                    print("1. Nombre")
                    print("2. Fecha")
                    print("3. Estado")
                    print("4. Fabricante")

                    opcion = valid_int("Ingrese el número correspondiente a la opción que desea editar: ")

                    if opcion == 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para mantener el actual): ")
                        implante.asignarNombre(nuevo_nombre)
                    elif opcion == 2:
                        nueva_fecha = input("Ingrese la nueva fecha (deje en blanco para mantener la actual): ")
                        implante.asignarFecha(nueva_fecha)
                    elif opcion == 3:
                        nuevo_estado = input("Ingrese el nuevo estado (deje en blanco para mantener el actual): ")
                        implante.asignarEstado(nuevo_estado)
                    elif opcion == 4:
                        nuevo_fabricante = input("Ingrese el nuevo fabricante (deje en blanco para mantener el actual): ")
                        implante.asignarFabricante(nuevo_fabricante)
                    else:
                        print("-----------------------------------")
                        print("Opción no válida. Intente de nuevo.")
                        print("-----------------------------------")
                        continue

                    print("-----------------------------------------------------")
                    print(f"Implante con ID {id_implante} editado correctamente.")
                    print("-----------------------------------------------------")
                    return

        print("------------------------------------------------------------------")
        print(f"No se encontró un implante con ID {id_implante} en el inventario.")
        print("------------------------------------------------------------------")


    def visualizar_inventario(self):
        print("--------------------------")
        print("\nInventario de Implantes:")
        print("--------------------------")
    
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            for i, implante in enumerate(self.inventario, start=1):
                print(f"\nImplante {i}:")
                print(f"Nombre: {implante.verNombre()}")
                print(f"Tipo: {type(implante).__name__}")
                print(f"ID: {implante.verId()}")
        
                fecha_implante = implante.verFecha()
                if isinstance(fecha_implante, datetime):
                    fecha_formateada = fecha_implante.strftime("%d/%m/%Y")
                    print(f"Fecha: {fecha_formateada}")
                else:
                    print(f"Fecha: {fecha_implante}")

                print(f"Estado: {implante.verEstado()}")
                print(f"Fabricante: {implante.verFabricante()}")

        print("--------------------------------------------------------------")
            
def main():
    sis = Sistema()

    while True:
        print("""\n1. Agregar Implante y asignarlo a un paciente
            2. Eliminar Implante
            3. Editar Información de Implante
            4. Visualizar Inventario
            5. Agregar paciente
            6. Visualizar paciente
            7. Seguimiento de implantes
            8. Salir""")

        opcion = valid_int("Seleccione una opción (1-5): ")

        if opcion == 1:
            #agregar implante y asignar a paciente
            sis.agregar_implante()
            cedula_paciente = valid_int("Ingrese la cédula del paciente al que se asignará el implante: ")
            paciente = sis.obtenerPaciente()
            if paciente:
                implante = sis.inventario[-1] #toma el ultimo implante agregado al inventario
                fecha_implantacion = valid_date("Ingrese la fecha de implantación: ")
                medico_responsable = valid_letter("Ingrese el médico responsable: ")
                estado_implante = valid_letter("Ingrese el estado del implante: ")

                sis.asignarImplanteAPaciente(cedula_paciente, implante, fecha_implantacion, medico_responsable, estado_implante)
            else:
                print("------------------------------------------------------------")
                print(f"No se encontro un paciente con la cédula {cedula_paciente}.")
                print("------------------------------------------------------------")

        elif opcion == 2:
            sis.eliminar_implante()
            
        elif opcion == 3:
            sis.editar_implante()
            
        elif opcion == 4:
            sis.visualizar_inventario()
            if not sis.inventario:
                print("-------------------------")
                print("El inventario está vacío.")
                print("-------------------------")
            
        elif opcion == 5:
            #agregar paciente 
            paciente_nuevo = Paciente()
            paciente_nuevo.asignarNombre(valid_letter("Ingrese el nombre del paciente: "))
            paciente_nuevo.asignarCedula(valid_int("Ingrese la cedula del paciente: "))
            paciente_nuevo.asignarGenero(valid_letter("Ingrese el genero del paciente: "))
            paciente_nuevo.asignarMedico(valid_letter("Ingrese el medico responsable del paciente: "))
            sis.agregarPacientes(paciente_nuevo)
            print("--------------------------------------------------------------")
            print(f"Paciente {paciente_nuevo.verNombre()} registrado correctamente.")
            print("--------------------------------------------------------------")
            
        elif opcion == 6:
            paciente = sis.obtenerPaciente()
            if paciente:
                sis.mostrarDetallesPaciente(paciente)  
            
        elif opcion == 7:
            #seguimiento de implantes
            id_implante = valid_int("Ingrese el ID del implante para realizar seguimiento: ")

            # Verificar si el ID del implante existe en el inventario
            implante_seleccionado = None
            for implante in sis.inventario:
                if implante.verId() == id_implante:
                    implante_seleccionado = implante
                    break

            if implante_seleccionado:
                fecha_revision = valid_date("Ingrese la fecha de revisión (formato: DD/MM/YYYY): ")
                estado_implante = valid_letter("Ingrese el nuevo estado del implante: ")
                sis.realizarSeguimientoImplante(id_implante, fecha_revision, estado_implante)
    
            else:
                print("-------------------------------------------------")
                print(f"No se encontró un implante con ID {id_implante}.")
                print("-------------------------------------------------")
            
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
