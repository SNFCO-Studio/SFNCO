import pymysql

output = []


class index:
    def __init__(self, data: dict):
        self.db = pymysql.connect(host=data["host"],
                                  port=data["port"],
                                  user=data["user"],
                                  password=data["passwd"],
                                  db=data["db"],
                                  charset="utf8")

    def qRead(self, column: str, fm: str):
        cursor = self.db.cursor()
        cursor.execute("SELECT " + column + " FROM " + fm)
        data = cursor.fetchall()
        for key in range(len(data)):
            output.append(list(data[key]))
        return output

    def qSelect(self, fm: str, key: str, value: str):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM " + fm + " WHERE " + key + " =\'" + value + "\'")
        data = cursor.fetchall()
        for key in range(len(data)):
            output.append(list(data[key]))
        return output

    def qDelete(self, fm: str, key: str, value: str):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM " + fm + " WHERE " + key + "=\'" + value + "\'")
        data = cursor.fetchall()
        for key in range(len(data)):
            output.append(list(data[key]))
        return output
