class Services():
    def __init__(self, id_service, description, price):
        self.id_service = id_service
        self.description = description
        self.price = price

        @property
        def get_id_service(self):
            return self.id_service

        @property
        def get_description(self):
            return self.description

        @property
        def get_price(self):
            return self.price