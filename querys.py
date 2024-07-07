from psycopg2 import connect


class QueryUser:
    def __init__(self) -> None:
        self.conn = connect("postgresql://postgres:postgres@localhost/postgres")
        self.cursor = self.conn.cursor()

    def create_new_user(self, name, citzen_id):
        statement = f"INSERT INTO user IF NOT EXISTS(id, name, citzen_id) values ({name}, {citzen_id})"
        self.cursor.execute(statement)