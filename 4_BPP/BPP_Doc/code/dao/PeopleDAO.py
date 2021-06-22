"""
    Clase que de acceso a la BD para trabajar con el objeto persona
"""
import sqlite3
from sqlite3 import Error
from model.Person import person


class people_dao:

    def create(conn):
        """
            Metodo que crea la tabla de personas en BD
        """
        try:
            sql = """ CREATE TABLE IF NOT EXISTS People (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            surname text NOT NULL,
                            age integer,
                            job text
                        ); """

            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def insert(conn, person):
        """
            Metodo que inserta una persona en BD
        """

        sql = """ INSERT INTO People (name, surname, age, job)
                VALUES(?,?,?,?); """

        try:
            cur = conn.cursor()
            params = (person.name, person.surname, person.age, person.job)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Person has been added ")
            return cur.lastrowid
        except Error as e:
            print(e)

    def update(conn, person):
        """
            Metodo que actualiza una persona en BD
        """

        sql = """ UPDATE People
                SET name = ?, surname = ?, age = ?, job = ?
                WHERE id = ? """

        try:
            cur = conn.cursor()
            params = (person.name, person.surname, person.age, person.job,
                      person.id)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Person has been updated ")
        except Error as e:
            print(e)

    def select_all(conn):
        """
            Metodo que busca todas las personas en BD
        """
        try:
            cur = conn.cursor()
            cur.execute(" SELECT * FROM People")
            rows = cur.fetchall()

            for row in rows:
                print("DB Message: " + str(row))

        except Error as e:
            print(e)

    def delete(conn, person):
        """
            Metodo que elimina una persona en BD
        """
        try:
            cur = conn.cursor()
            sql = " DELETE FROM People WHERE id = ? "
            params = (person.id,)
            cur.execute(sql, params)
            conn.commit()
            print("DB Message: Person has been deleted ")

        except Error as e:
            print(e)
