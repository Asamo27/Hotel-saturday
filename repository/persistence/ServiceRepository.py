from domain.model.Services import Services


class ServiceRepository:
    def __init__(self):
        self.service = Services

    def create_service_repository(self, service, db):
        query = "INSERT INTO Services (id_service, description, price) VALUES (%s, %s, %s)"
        values = (service.id_service, service.description, service.price)
        reponse = db.execute_query(query, values)
        return reponse

    def find_all_services(self, db):
            query = "SELECT * FROM Services"
            response = db.execute_query(query)
            return response

    def update_service(self, service, db):
        query = "UPDATE Services SET description = %s, price = %s  WHERE id_service = %s"
        values = (service.description, service.price, service.id_service)
        response = db.execute_query(query, values)
        return response

    def delete_service(self, id_service, db):
        query = "DELETE FROM Services WHERE id_service = %s"
        values = (id_service,)
        response = db.execute_query(query,values)
        return response