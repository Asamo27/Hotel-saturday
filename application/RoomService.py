from domain.model.Room import Room


class RoomService:

    register_room = []

    def __init__(self):
        self.room = Room(None, None)

    def create_room(self, room):
        room.room_number = self.register_room[0]
        room.room_type = self.register_room[1]
        room.available = self.register_room[2]

    def book_room(self,room_number):
        for room in self.register_room:
            if room.room_number == room_number:
                room.mark_available(False)
                return True
        return False

    def print_all_rooms(self):
        for data in self.register_room:
            print(data)