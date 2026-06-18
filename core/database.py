import psycopg2


class Database:

    def __init__(
        self,
        host,
        database,
        user,
        password,
        port=5432
    ):

        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

    def execute(
        self,
        query,
        params=None
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            params
        )

        try:
            rows = cursor.fetchall()

        except Exception:
            rows = []

        cursor.close()

        return rows

    def close(self):

        if self.connection:
            self.connection.close()