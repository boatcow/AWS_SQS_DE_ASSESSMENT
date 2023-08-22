# This file provides a class to connect and perform CRUD operations on a PostgreSQL database.

import psycopg2

class PostgresConnector:
    """
    A class used to connect to a PostgreSQL database and perform CRUD operations.
    """
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        """
        Initializes the PostgresConnector with the given database credentials.

        :param dbname: Name of the database
        :param user: Username for the database connection
        :param password: Password for the database connection
        :param host: Database host (default is "localhost")
        :param port: Database port (default is "5432")
        """
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = self.connection.cursor()

    def post(self, table_name, columns, values):
        """
        Inserts a new row into the specified table.

        :param table_name: Name of the table to insert into
        :param columns: List of column names
        :param values: Tuple of values corresponding to the columns
        """
        column_string = ', '.join(columns)
        placeholders = ', '.join('%s' for _ in range(len(columns)+1))
        
        query = f"INSERT INTO {table_name} ({column_string}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def get(self, table, columns="*", where=None):
        """
        Retrieves data from the specified table.

        :param table: Name of the table to retrieve from
        :param columns: Column names to retrieve (default is all columns "*")
        :param where: WHERE clause (default is None)

        :return: List of retrieved rows
        """
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += f" WHERE {where}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def put(self, table, set_column, set_value, where_column, where_value):
        """
        Updates a specified row in the table.

        :param table: Name of the table to update
        :param set_column: Name of the column to update
        :param set_value: New value for the set_column
        :param where_column: Column to use in the WHERE clause
        :param where_value: Value to use in the WHERE clause for where_column
        """
        query = f"UPDATE {table} SET {set_column} = %s WHERE {where_column} = %s"
        self.cursor.execute(query, (set_value, where_value))
        self.connection.commit()

    def delete(self, table, where_column, where_value):
        """
        Deletes a specified row from the table.

        :param table: Name of the table to delete from
        :param where_column: Column to use in the WHERE clause
        :param where_value: Value to use in the WHERE clause for where_column
        """
        query = f"DELETE FROM {table} WHERE {where_column} = %s"
        self.cursor.execute(query, (where_value,))
        self.connection.commit()

    def close(self):
        """
        Closes the cursor and the database connection.
        """
        self.cursor.close()
        self.connection.close()