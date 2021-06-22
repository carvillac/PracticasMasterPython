"""
    Clase que de acceso a la BD para trabajar con el objeto coche
"""
import sqlite3
from sqlite3 import Error
from model.Car import car


class cars_dao:

    def create(conn):
        """
            Metodo que crea la tabla de coches en BD
        """
        try:
            sql = """ CREATE TABLE IF NOT EXISTS Cars (
                            id integer PRIMARY KEY,
                            brand text NOT NULL,
                            model text NOT NULL
                        ); """

            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def insert(conn, car):
        """
            Metodo que inserta un coche en BD
        """

        sql = """ INSERT INTO Cars (brand, model)
                VALUES(?,?); """

        try:
            cur = conn.cursor()
            params = (car.brand, car.model)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Car has been added ")
            return cur.lastrowid
        except Error as e:
            print(e)

    def update(conn, car):
        """
            Metodo que actualiza un coche en BD
        """

        sql = """ UPDATE Cars
                SET brand = ?, model = ?
                WHERE id = ? """

        try:
            cur = conn.cursor()
            params = (car.brand, car.model, car.id)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Car has been updated ")
        except Error as e:
            print(e)

    def select_all(conn):
        """
            Metodo que busca todos los coches en BD
        """
        try:
            cur = conn.cursor()
            cur.execute(" SELECT * FROM Cars")
            rows = cur.fetchall()

            for row in rows:
                print("DB Message: " + str(row))

        except Error as e:
            print(e)

    def delete(conn, car):
        """
            Metodo que borra un ccohe en BD
        """
        try:
            cur = conn.cursor()
            sql = " DELETE FROM Cars WHERE id = ? "
            params = (car.id,)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Car has been deleted ")

        except Error as e:
            print(e)
