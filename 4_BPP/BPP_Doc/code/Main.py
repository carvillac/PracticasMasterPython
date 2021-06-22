"""
    Función principal
"""
import sqlite3
from sqlite3 import Error
from dao.PeopleDAO import people_dao
from dao.CarsDAO import cars_dao
from model.Person import person
from model.Car import car

conn = None
try:
    conn = sqlite3.connect("database.db")

    people_dao.create(conn)
    cars_dao.create(conn)

    person1 = person("Carlos", "Villacastín", "36", "Informático")
    id = people_dao.insert(conn, person1)
    person1.set_id(id)

    person2 = person("Natalia", "Sanchez", "33", "Enfermera")
    id = people_dao.insert(conn, person2)
    person2.set_id(id)

    person1.set_job("Ing. Informatico")
    people_dao.update(conn, person1)

    people_dao.select_all(conn)
    people_dao.delete(conn, person1)

    people_dao.select_all(conn)

    car1 = car("Renault", "Laguna")
    id = cars_dao.insert(conn, car1)
    car1.set_id(id)

    car2 = car("Citroen", "C3")
    id = cars_dao.insert(conn, car2)
    car2.set_id(id)

    car2.set_model("Picasso")
    cars_dao.update(conn, car2)

    cars_dao.select_all(conn)
    cars_dao.delete(conn, car1)

    cars_dao.select_all(conn)


except Error as e:
    print(e)
finally:
    if conn:
        conn.close
