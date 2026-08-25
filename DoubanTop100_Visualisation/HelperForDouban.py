import mysql.connector
import os
class MySqlHelper:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password= os.getenv("MYSQL_PASSWORD"),
            database="douban"
        )
    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def insert(self, sql):
        self.execute(sql)

    def update(self, sql):
        self.execute(sql)

    def delete(self, sql):
        self.execute(sql)

    def clear(self, table):
        sql = f"TRUNCATE TABLE {table}"
        self.execute(sql)