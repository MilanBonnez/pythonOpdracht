

import sqlite3

class Database:
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

    def getTable(self, table):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def addPerson(self, table, firstName, lastName):
        query = f"INSERT INTO {table} (firstName, lastName) VALUES ('{firstName}', '{lastName}')"
         self.cursor.execute(query)
         self.con.commit()

      def deletePerson(self, personId, table):
        query = f"DELETE FROM {table} WHERE id = {personId}"
        self.cursor.execute(query)
        self.con.commit()


    def showPerson(self, personId, table):
        query = f"SELECT * FROM {table} WHERE user_id = {personId}"
        self.cursor.execute(query)
        person = self.cursor.fetchall()
        return person
