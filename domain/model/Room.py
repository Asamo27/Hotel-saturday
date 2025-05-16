class Room:
    def __init__(self, room_number, room_type, available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.available = available

    @property
    def get_room_number(self):
        return self.room_number

    @property
    def get_type(self):
        return self.room_type

    def mark_available(self, available):
        self.available = available

    def __str__(self):
        availability = "Disponible" if self.available else "No disponible"
        return f"Número {self.room_number}, Tipo: {self.room_type}, Estado: {availability}"