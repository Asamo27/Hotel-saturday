from application.ReservationService import ReservationService
from domain.model.Reservation import Reservation
from repository.persistence.ReservationRepository import ReservationRepository
from datetime import datetime

class ReservationInput:
    def __init__(self):
        self.reservation = Reservation(
            id_reservation=None,
            id_guest=None,
            id_employee=None,
            room_number=None,
            id_service=None,
            booking_date=None,
            start_date=None,
            end_date=None,
            estado='confirmada'
        )
        self.reservation_repository = ReservationRepository()
        self.reservation_service = ReservationService()

    def register(self, db):
        id_reservation = input("Ingrese ID de la reserva: ")
        self.reservation.id = id_reservation

        id_guest = input("Ingrese ID del huésped: ")
        self.reservation.id_guest = id_guest

        id_employee = input("Ingrese ID del empleado: ")
        self.reservation.id_employee = id_employee

        room_number = input("Ingrese número de habitación: ")
        self.reservation.room_number = room_number

        id_service = input("Ingrese ID del servicio: ")
        self.reservation.id_service = id_service

        booking_date = input("Ingrese fecha de reserva (YYYY-MM-DD): ")
        start_date = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
        end_date = input("Ingrese fecha de fin (YYYY-MM-DD): ")

        # Conversión de string a fecha
        self.reservation.booking_date = datetime.strptime(booking_date, "%Y-%m-%d").date()
        self.reservation.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.reservation.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        estado = input("Ingrese estado (confirmada / cancelada / finalizada): ")
        self.reservation.estado = estado

        self.reservation_repository.create_reservation_repository(self.reservation, db)

    def print_data(self):
        self.reservation_service.print_all_reservations()