class Sistema:
    def __init__(self):
        self.__paciente = {}
        self.inventario = []  

    def agregarPaciente(self, paciente):
        self.__pacientes[paciente.verCedula()] = paciente
        print("----------------------------------------------------------")
        print(f"Paciente {paciente.verNombre()} registrado correctamente.")
        print("----------------------------------------------------------")
        
    def obtenerPaciente(self, cc):
        return self.__paciente.get(cc)
    
    def asignarImplanteAPaciente(self, cedula, implante, fecha_implantacion, medico_responsable, estado_implante):
        paciente = self.__pacientes.get(cedula)
        if paciente:
            implante.asignarFecha(fecha_implantacion)
            implante.asignarEstado(estado_implante)
            # Agregar información adicional si es necesario, como el médico responsable
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
                # Registrar la fecha de revisión
                # Agregar cualquier otra información de seguimiento si es necesario
                print("-------------------------------------------------------------")
                print(f"Seguimiento realizado para el implante con ID {id_implante}.")
                print("-------------------------------------------------------------")
                return
        print("-------------------------------------------------")
        print(f"No se encontró un implante con ID {id_implante}.")
        print("-------------------------------------------------")

    def agregar_implante(self):
        tipo_implante = valid_letter("Ingrese el tipo de implante (Protesis_C, Marcapasos, Stents, ImplantesD, Protesis_R): ")

        if tipo_implante == "Protesis_C":
            implante = Protesis_C()
        
        elif tipo_implante == "Marcapasos":
            implante = Marcapasos()
            
        elif tipo_implante == "Stents":
            implante = Stents()
           
        elif tipo_implante == "ImplantesD":
            implante = ImplantesD()
            
        elif tipo_implante == "Protesis_R":
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
        id_implante = int(input("Ingrese el ID del implante que desea eliminar: "))

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
            print(f"\nTipo: {type(implante).__name__}")
            print(f"ID: {implante.verId()}")
            # Muestra otros detalles comunes y específicos del implante
            # ...

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
            tipo_implante = input("Ingrese el tipo de implante (Protesis_C, Marcapasos, Stents, ImplantesD, Protesis_R): ")
            implante = None

            # Crear instancia de tipo de implante según la opción ingresada

            # Solicitar detalles específicos del implante

            # Solicitar información sobre el paciente al que se asignará el implante
            cedula_paciente = input("Ingrese la cédula del paciente al que se asignará el implante: ")
            fecha_implantacion = input("Ingrese la fecha de implantación: ")
            medico_responsable = input("Ingrese el médico responsable: ")
            estado_implante = input("Ingrese el estado del implante: ")

            sis.asignarImplanteAPaciente(cedula_paciente, implante, fecha_implantacion, medico_responsable, estado_implante)
        elif opcion == 2:
            #eliminar implante
            sis.eliminar_implante()
        elif opcion == 3:
            #editar implante
            sis.editar_implante()
        elif opcion == 4:
            #ver inventario
            sis.visualizar_inventario()
        elif opcion == 5:
            #agregar paciente
            paciente = Paciente()
            # Solicitar detalles del paciente
            sistema.agregarPaciente(paciente)
        elif opcion == 6:
            #obtener paciente
            sis.obtenerPaciente()
        elif opcion == 7:
            #seguimiento de implantes
            id_implante = input("Ingrese el ID del implante para realizar seguimiento: ")
            fecha_revision = input("Ingrese la fecha de revisión: ")
            estado_implante = input("Ingrese el nuevo estado del implante: ")

            sis.realizarSeguimientoImplante(id_implante, fecha_revision, estado_implante)
        elif opcion == 8:
            print("-------------")
            print("¡Hasta luego!")
            break
        else:
            print("-----------------------------------")
            print("Opción no válida. Intente de nuevo.")
            print("-----------------------------------")
            
if __name__ == "__main__":
    main()
