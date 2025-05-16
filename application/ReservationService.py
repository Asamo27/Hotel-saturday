from domain.model.Reservation import Reservation

class ReservationService:
    def __init__(self):
        self.reservations = []  # Almacenar objetos Reservation

    def create_reservation(self, reservation: Reservation):

        self.reservations.append(reservation)
        print(f"Reserva {reservation.id} creada con éxito para el huésped {reservation.id_guest}.")

    def cancel_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation.id == reservation_id:
                if reservation.estado != 'cancelada':
                    reservation.estado = 'cancelada'
                    print(f"Reserva {reservation_id} cancelada exitosamente.")
                    return True
                else:
                    print(f"La reserva {reservation_id} ya está cancelada.")
                    return False
        print(f"No se encontró la reserva con ID {reservation_id}.")
        return False

    def get_reservation_by_id(self, reservation_id):

        for reservation in self.reservations:
            if reservation.id == reservation_id:
                return reservation
        print(f"No se encontró la reserva con ID {reservation_id}.")
        return None

    def print_all_reservations(self):
        if not self.reservations:
            print("No hay reservas registradas.")
            return

        print("📋 Lista de Reservas:\n")
        for reservation in self.reservations:
            print(f"ID: {reservation.id}, Huésped ID: {reservation.id_guest}, "
                  f"Estado: {reservation.estado}, Fecha de inicio: {reservation.start_date}, "
                  f"Fecha de fin: {reservation.end_date}")