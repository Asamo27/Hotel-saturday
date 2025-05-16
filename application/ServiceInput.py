from application.ServicesService import ServicesService
from domain.model.Services import Services
from repository.persistence.ServiceRepository import ServiceRepository


class ServiceInput:
    def __init__(self):
        self.services_service = ServicesService()
        self.service = Services(None, None, None)
        self.service_repository = ServiceRepository()

    def register(self, service, db):
        id_service = input("Ingrese el id del servicio")
        self.service.id_service = id_service
        description = input("Ingrese descripcion del servicio")
        self.service.description = description
        price = int(input("Ingrese el precio del servicio"))
        self.service.price = price
        self.service_repository.create_service_repository(self.service, db)

    def print_data(self):
        self.services_service.print_all_services()