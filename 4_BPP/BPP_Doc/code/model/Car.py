"""
    Clase que modela un coche.

    Atributos:
    ----------
    id:
        Identificador único en BD
    brand:
        Marca del vehiculo
    model:
        Modelo del vehiculo
"""


class car:

    def __init__(self, brand, model):
        """
            Constructor
        """
        try:
            self.brand = brand
            self.model = model
        except Exception:
            print("There was an error in the input numbers")

    def get_id(self):
        """
            Devuelve el ID
        """
        return self.id

    def set_id(self, id):
        """
            Setea el ID
        """
        self.id = id

    def get_brand(self):
        """
            Devuelve la marca
        """
        return self.brand

    def set_brand(self, brand):
        """
            Setea la marca
        """
        self.brand = brand

    def get_model(self):
        """
            Devuelve el modelo
        """
        return self.model

    def set_model(self, model):
        """
            Setea el modelo
        """
        self.model = model
