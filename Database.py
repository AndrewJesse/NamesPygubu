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

    def fetch_names(cls):
        from Name import NameFetcher
        sql = "SELECT Name, Year, Gender, NameCount, Total FROM all_data WHERE Name = 'Marc' AND Gender = 'M' ORDER BY Year;"