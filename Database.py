import pyodbc

class Database:
    # Connect to the database using the CIS 275 student account.
    __connection = None
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            trustedconnection = 'yes'
            trustservercertificate = 'yes'
            try:
                cls.__connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                    + ';UID=' + username + ';PWD=' + password
                    + ';trustedconnection=' + trustedconnection
                    + ';trustservercertificate=' + trustservercertificate)
            except pyodbc.InterfaceError:
                cls.__connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                    + ';UID=' + username + ';PWD=' + password)

    @classmethod
    def fetch_names(cls, name, gender):
        from Name import Name
        sql = "SELECT Name, Year, Gender, NameCount, Total FROM all_data WHERE Name = ? AND Gender = ? ORDER BY Year;"
        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql, (name, gender))
        print(name, gender)
        names = []
        for row in cursor:
            name_obj = Name(row[0], row[1], row[2], row[3], row[4])
            names.append(name_obj)
        return names


