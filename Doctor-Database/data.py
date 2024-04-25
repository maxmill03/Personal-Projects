import sqlite3
from doctor import Doctor


class DoctorDataProcessor:
    def __init__(self):
        self.doctor_list = []

    def load_doctors(self, sql_database):
        connection = sqlite3.connect(sql_database)
        cursor = connection.cursor()
        for row in cursor.execute("SELECT * FROM healthfirst_doctors ORDER BY FullName"):
            self.doctor_list.append(Doctor(row[0], row[1], row[2], row[4]))  # list of doctor objects

    def get_doctors(self):
        return self.doctor_list  # return list of doctors
