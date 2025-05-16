class Reservation:
    def __init__(self, id_reservation, id_guest, id_employee, room_number, id_service,
                 booking_date, start_date, end_date, estado='confirmada'):
        self.id = id_reservation
        self.id_guest = id_guest
        self.id_employee = id_employee
        self.room_number = room_number
        self.id_service = id_service
        self.booking_date = booking_date
        self.start_date = start_date
        self.end_date = end_date
        self.estado = estado

    def __str__(self):
        return (
            f"Reservation Details:\n"
            f"  - ID           : {self.id}\n"
            f"  - Guest ID     : {self.id_guest}\n"
            f"  - Employee ID  : {self.id_employee}\n"
            f"  - Room Number  : {self.room_number}\n"
            f"  - Service ID   : {self.id_service}\n"
            f"  - Booking Date : {self.booking_date}\n"
            f"  - Start Date   : {self.start_date}\n"
            f"  - End Date     : {self.end_date}\n"
            f"  - Status       : {self.estado}"
        )
