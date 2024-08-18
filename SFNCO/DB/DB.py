from SFNCO.DB.Mysql.index import index


class DB:
    pass


class connect:
    def __init__(self, host: str, port: int, user: str, passwd: str):
        self.data: dict = {
            "host": host,
            "port": port,
            "user": user,
            "passwd": passwd
        }

    def Mysql(self, Db: str):
        self.data["db"] = Db
        return index(self.data)
