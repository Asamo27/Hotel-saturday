from domain.model.Services import Services

class ServicesService:
    register_data = []

    def __init__(self):
        self.service = Services(None, None, None)

    def createService(self, service):
        service.id_service = self.register_data[0]
        service.description = self.register_data[1]
        service.price = self.register_data[2]

    def print_all_services(self=None):
        for service in self.register_data:
            print(service)