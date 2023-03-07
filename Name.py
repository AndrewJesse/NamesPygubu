from Database import Database


class Name:
    pass
class NameFetcher:
    @staticmethod
    def Names():
        return Database.fetch_names()
