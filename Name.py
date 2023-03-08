from Database import Database


class Name:

    def __init__(self, name, year, gender, nameCount, total):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__nameCount = nameCount
        self.__total = total

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_gender(self):
        return self.__gender

    def get_name_count(self):
        return self.__nameCount

    def get_total(self):
        return self.__total

    @staticmethod
    def fetch_names(name, gender):
        from Database import Database
        return Database.fetch_names(name, gender)
