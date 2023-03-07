import pyodbc


class Database:
    __connection = None

    # Connect to the database using the CIS 275 student account.
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'IMDB'
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
