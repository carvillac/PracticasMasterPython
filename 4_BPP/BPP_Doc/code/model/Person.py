"""
    Clase que modela una persona.

    Atributos:
    ----------
    id:
        Identificador único en BD
    name:
        Nombre de la persona
    surname:
        Apellido de la persona
    age:
        Edad de la persona
    job:
        Trabajo de la persona
"""


class person:

    def __init__(self, name, surname, age, job):
        """
            Constructor
        """
        try:
            self.name = name
            self.surname = surname
            self.age = int(age)
            self.job = job
        except Exception:
            print("There was an error in the input numbers")

    def get_id(self):
        """
            Devuelve el ID
        """
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        """
            Devuelve el nombre
        """
        return self.name

    def set_name(self, name):
        """
            Setea el nombre
        """
        self.name = name

    def get_surname(self):
        """
            Devuelve el apellido
        """
        return self.surname

    def set_surname(self, surname):
        """
            Setea el apellido
        """
        self.surname = surname

    def get_age(self):
        """
            Devuelve la edad
        """
        return self.age

    def set_age(self, age):
        """
            Setea la edad
        """
        self.age = age

    def get_job(self):
        """
            Devuelve el trabajo
        """
        return self.job

    def set_job(self, job):
        """
            Setea el trabajo
        """
        self.job = job
