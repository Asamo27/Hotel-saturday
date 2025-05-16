import time

from application.EmployeeInput import EmployeeInput
from application.ServiceInput import ServiceInput
from domain.model.Guest import Guest
from application.GuestInput import GuestInput
from domain.model.Reservation import Reservation
from application.ReservationInput import ReservationInput
from repository.persistence.ReservationRepository import ReservationRepository
from application.RoomInput import RoomInput
from repository.connection.conexionBD import Conexion
from domain.model.Room import Room
from repository.persistence.EmployeeRepository import EmployeeRepository
from repository.persistence.RoomRepository import RoomRepository
from domain.model.Employee import Employee
from domain.model.Services import Services
from repository.persistence.ServiceRepository import ServiceRepository


class MenuApp:
    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel')
        self.db.connection()
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_input = GuestInput()
        self.room_input = RoomInput()
        self.room = Room(None, None)
        self.room_repository = RoomRepository
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_input = EmployeeInput()
        self.employee_repository = EmployeeRepository
        self.service = Services(None, None, None)
        self.service_input = ServiceInput()
        self.service_repository = ServiceRepository()
        self.reservation = Reservation(None, None, None, None, None, None, None, None)
        self.reservation_input = ReservationInput()
        self.reservation_repository = ReservationRepository()



## menu
    def init_app(self):
        print("\n¡Bienvenidos a la interfaz de la Administración del Hotel Saturday.!")
        init = int(input("\nPulse 1 para comenzar, 0 para cerrar: "))

        while init != 0:
            print("-- MAIN MENU --")
            print(" 1. Iniciar Sesion")
            print(" 2. Registro de un nuevo cliente")
            print(" 3. Gestión de Reservas del cliente")
            print(" 4. Gestión de Habitaciones para el cliente")
            print(" 5. Sesion para Empleados")
            print(" 6. Sesion para Servicios")
            print(" 0. Salir del sistema")

            option = input("\nElija una opción: ")

            try:
                option = int(option)

                if option == 0:
                    print("\n¡Gracias por utilizar el sistema! ¡Nos vemos pronto!")
                    init = 0
                elif option == 1:
                    self.login_menu()
                elif option == 2:
                    print("-- REGISTRO PARA HUÉSPEDES --")
                    self.guest_input.register(self.guest, self.db)
                elif option == 3:
                    self.reservation_menu()
                elif option == 4:
                    self.room_menu()
                elif option == 5:
                    self.employee_menu()
                elif option == 6:
                    self.service_menu()
                else:
                    print("\n⚠️ Ingrese una opción válida para continuar, porfavor intente nuevamente.⚠️ ")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.⚠️ ")

    def login_menu(self):
        print("-- Iniciar Sesion --")
        print("Funcionalidad de login en desarrollo...")
        input("\nPresione Enter para continuar...")

    def reservation_menu(self):

        while True:
            print("-- GESTIÓN DE RESERVAS DEL USUARIO --")
            print(" 1. Consultar una reserva")
            print(" 2. Generar una nueva reserva para el cliente")
            print(" 0. Regresar al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    print("\n✅ Has consultado exitosamente")
                    naureser = self.reservation_repository.get_all_reservations(self.db)
                    print(naureser)
                elif option == 2:
                    print("\nComenzando con el proceso de reserva...")
                    print(" 1. Comprobar disponibilidad \n 2. Salir")
                    option = int(input())
                    if option == 1:
                        print("\nGenerando un listado de habitaciones...")
                        rooms = self.room_input.room_repository.find_all(self.db)
                        print(rooms)
                        print("Continua el proceso de reserva")
                        numr = input("Ingrese el numero de la habitación a reservar")
                        time.sleep(5)
                        if self.room_repository.is_available(None, numr, self.db):
                            print("Reservando la Habitación..")
                            self.reservation_input.register(self.db)
                        else:
                            print("Ups ... !Lamentamos informarte que la habitación que elegiste no está disponible!. Intenta con otra.")
                    else:
                        break
                else:
                    print("\n⚠️ Ingrese una opción válida para continuar, porfavor intente nuevamente.⚠️ ")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def room_menu(self):
        while True:
            print("GESTIÓN DE HABITACIONES")
            print(" 1. Listar todas las habitaciones")
            print(" 2. Buscar habitación por número")
            print(" 3. Registrar nueva habitación")
            print(" 4. Mostrar habitaciones disponibles")
            print(" 5. Actualizar disponibilidad")
            print(" 6. Eliminar habitación")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    print("\nListando habitaciones...")
                    rooms = self.room_input.room_repository.find_all(self.db)
                    print(rooms)
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    number = input("Ingrese el número de habitación")
                    room_id = self.room_input.room_repository.find_by_room_numer(number, self.db)
                    print(room_id)
                    print("\n✅ Encontraste la habitación")
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    self.room_input.register(self.room, self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    print("\nListando habitaciones disponibles...")
                    reponse = self.room_repository.find_available(None, self.db)
                    print(reponse)
                    input("\nPresione Enter para continuar...")
                elif option == 5:
                    print("\nActualizar disponibilidad de habitación...")
                    number = input("\nIngrese el número de habitación...")
                    room = input("\nIngrese el estado de la habitación...")
                    updated = self.room_input.room_repository.update_availability(number, room, self.db)
                    print(updated)
                elif option == 6:
                    print("\nFuncionalidad de eliminación en desarrollo...")
                    number = input("\nPresione número de habitación a eliminar...")
                    delete = self.room_input.room_repository.delete(number, self.db)
                    print(delete)
                else:
                    print("\n⚠️ Ingrese una opción válida para continuar, porfavor intente nuevamente.⚠️ ")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def employee_menu(self):
        while True:
            print("-- GESTIÓN DE EMPLEADOS --")
            print(" 1. Generar un listado de todos los empleados del sistema")
            print(" 2. Registrar nuevo empleado")
            print(" 3. Actualizar un empleado existente")
            print(" 4. Remover un empleado")
            print(" 0. Regresar al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    anothernau = self.employee_repository.find_all_employees(None, self.db)
                    print(anothernau)
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    self.employee_input.register(self.employee, self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    id_employee = input("Ingrese el número del empleado a actualizar: ")
                    name = input("Nombre del empleado: ")
                    last_name = input("Apellido del empleado: ")
                    phone = input("Ingresa el nuevo numero: ")
                    email = input("Email del empleado: ")
                    password = input("Contraseña nueva: ")
                    status = input("Estado: ")
                    salary = input("salario: ")
                    self.employee = Employee(id_employee, name, last_name, phone, email, password, status, salary)
                    result = self.employee_repository.update(None, self.employee, self.db)
                    print(result)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    number = input("Ingrese el número de identificación del empleado que quiere eliminar")
                    result = self.employee_repository.delete(None, number, self.db)
                    print(result)
                    input("\nPresione Enter para continuar...")
                else:
                    print("\n⚠️ Ingrese una opción válida para continuar, porfavor intente nuevamente.⚠️ ")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def service_menu(self):
        while True:
            print("-- GESTIÓN DE SERVICIOS --")
            print(" 1. Listar todos los servicios")
            print(" 2. Registrar nuevo servicio")
            print(" 3. Actualizar servicio")
            print(" 4. Eliminar servicio")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    nauanother  = self.service_repository.find_all_services(self.db)
                    print(nauanother)
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    self.service_input.register(self.service, self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    id_service = input("Ingrese el id del servicio que desea actualizar: ")
                    description = input("Ingrese la descripción del servicio: ")
                    price = input("Ingrese el costo del servicio: ")
                    self.service = Services(id_service, description, price)
                    update = self.service_repository.update_service(self.service, self.db)
                    print(update)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    id_service = input("Ingrese el id del servicio que desea eliminar: ")
                    delete = self.service_repository.delete_service(id_service, self.db)
                    print(delete)
                    input("\nPresione Enter para continuar...")
                else:
                    print("\n⚠️ Ingrese una opción válida para continuar, porfavor intente nuevamente.⚠️ ")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")