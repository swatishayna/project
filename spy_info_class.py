import spy_details

class Spy_Info:
    name = ""
    salutation = ""
    age = 0
    rating = 0.0
    is_online = True
    chats = []

    def __init__(self, salutation, name, age, rating, status):
        self.salutation = salutation
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = status

    def set_details(self, name, salutation, age, rating, is_online):
        self.name = name
        self.salutation = salutation
        self.rating = rating
        self.age = age
        self.is_online = is_online

    def displayDetails(self):
        print self.Name, " ", self.Age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_rating(self):
        return self.rating
    def get_salutation(self):
        return self.salutation
    def get_online(self):
        return self.is_online
    def get_chats(self):
        return self.chats
    def clear_chats(self):
        self.chats=[]