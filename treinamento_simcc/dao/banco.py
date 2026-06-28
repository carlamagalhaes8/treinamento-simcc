import psycopg2


class Connection:
    def __init__(self):
        self.database = "BD_PESQUISADOR"
        self.user = "postgres"
        self.password = "qualquer_uma"
        self.host = "localhost"
        self.port = 5437
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.database,
            user=self.user,
            host=self.host,
            password=self.password,
            port=self.port,
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def select(self, script_sql: str, parameters: list = []):
        with self.connection.cursor() as cursor:
            cursor.execute(script_sql, parameters)
            return cursor.fetchall()

    def exec(self, script_sql: str, parameters: list = []):
        with self.connection.cursor() as cursor:
            cursor.execute(script_sql, parameters)
            self.connection.commit()

    def execmany(self, script_sql: str, parameters: list = []):
        with self.connection.cursor() as cursor:
            cursor.executemany(script_sql, parameters)
            self.connection.commit()