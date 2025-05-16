from domain.model.Reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self.reservation = Reservation

    def create_reservation_repository(self, reservation, db):
        query = """
        INSERT INTO reservation (id, id_guest, id_employee, room_number, id_service, booking_date, start_date, end_date, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            reservation.id, reservation.id_guest, reservation.id_employee, reservation.room_number,
            reservation.id_service, reservation.booking_date, reservation.start_date, reservation.end_date, reservation.estado
        )
        db.execute_query(query, values)

    def get_reservations_by_guest(self, guest_id, db):
        query = "SELECT * FROM reservation WHERE id_guest = %s"
        result = db.execute_query(query, (guest_id,))
        return result

    def get_all_reservations(self, db):
        query = "SELECT * FROM reservation"
        result = db.execute_query(query)
        return result