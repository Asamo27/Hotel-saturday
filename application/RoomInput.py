from application.RoomService import RoomService
from domain.model.Room import Room
from repository.persistence.RoomRepository import RoomRepository


class RoomInput:
    def __init__(self):
        self.room = Room(None, None, None)
        self.room_repository = RoomRepository()
        self.room_service = RoomService()

    def register(self, room, db):
        room_number = input("Ingrese su número de habitación")
        self.room.room_number = room_number
        room_type = input("Ingrese tipo de habitación")
        self.room.room_type = room_type
        availability = input("Ingrese 1 si la habitación está disponible o 2 si está ocupada: ")
        if availability == "1":
            self.room.available = 'Disponible'  # Disponible
        elif availability == "2":
            self.room.available = 'No disponible'  # Ocupada
        else:
            print("Entrada inválida. Por defecto, la habitación se marcará como no disponible.")
            self.room.available = 'Disponible'

        self.room_repository.create_room_repository(self.room, db)

    def print_data(self):
        self.room_service.print_all_rooms()