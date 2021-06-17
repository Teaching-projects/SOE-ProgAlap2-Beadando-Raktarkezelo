import sqlite3


class DB:
    def __init__(self, conn):
        self.conn = conn

    def Connect(self):
        """
        This code is return the connection.
        """
        return sqlite3.connect(self.conn)
