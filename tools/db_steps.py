class DataBase:
    def __int__(self, db_connections):
        self.db_connections = db_connections

    def db_users(self):
        cursor = self.db_connections.cursor
        cursor.execute("""SELECT username FROM auth_user""")
        users = []
        for name in cursor.fetchall():
            users.append(''.join(name))
        return users