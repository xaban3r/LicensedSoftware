import config
import psycopg2


class Database:
    def __init__(self):
        self.dbname = config.db_name
        self.user = config.user
        self.password = config.password
        self.host = config.host

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
            )
            self.cur = self.conn.cursor()
            print("Connected to database successfully!")
        except Exception as e:
            print("Unable to connect to the database.")
            print(e)

    def execute(self, query):
        try:
            self.cur.execute(query)
            print("Query executed successfully!")
        except Exception as e:
            print("Unable to execute the query.")
            print(e)

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Connection closed successfully!")


# Запросы
# на заданную дату список подразделений, на компьютерах которых
# установлено не лицензионное ПО;
"""
SELECT DISTINCT D.name_organization_division
FROM Computers C
JOIN Division D ON C.computer_division = D.name_organization_division
JOIN Software S ON C.software = S.software_name
WHERE AGE(C.date_end, C.date_start) > S.validity_period;
"""

# список лицензионного ПО, количество лицензий на это ПО (по
# убыванию) на заданную дату;

"""
SELECT S.software_name, COUNT(*) AS license_count
FROM Computers C
JOIN Software S ON C.software = S.software_name
WHERE CURRENT_DATE <= C.date_end
GROUP BY S.software_name
ORDER BY license_count DESC;
"""

# список подразделений, количество компьютеров у подразделения (по
# убыванию) на заданную дату.

"""
SELECT D.name_organization_division, COUNT(*) AS computer_count
FROM Computers C
JOIN Division D ON C.computer_division = D.name_organization_division
WHERE CURRENT_DATE BETWEEN C.date_start AND C.date_end
GROUP BY D.name_organization_division
ORDER BY computer_count DESC;
"""
