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
