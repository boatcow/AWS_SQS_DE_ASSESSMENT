import psycopg2

class PostgresConnector:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        print(dbname,user,password,host,port)
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = self.connection.cursor()

    def post(self, table_name, columns, values):

        column_string = ', '.join(columns)
        placeholders = ', '.join('%s' for _ in range(len(columns)+1))
        
        query = f"INSERT INTO {table_name} ({column_string}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def get(self, table, columns="*", where=None):
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += f" WHERE {where}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def put(self, table, set_column, set_value, where_column, where_value):
        query = f"UPDATE {table} SET {set_column} = %s WHERE {where_column} = %s"
        self.cursor.execute(query, (set_value, where_value))
        self.connection.commit()

    def delete(self, table, where_column, where_value):
        query = f"DELETE FROM {table} WHERE {where_column} = %s"
        self.cursor.execute(query, (where_value,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()