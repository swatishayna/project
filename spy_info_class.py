class Spy_Info:


    name = "James"
    salutation = "Mr."
    age = 45
    rating = 4.9
    is_online = True
    chats = []

    def set_details(self, name, salutation, age, rating, is_online):
        self.name = name;
        self.salutation = salutation;
        self.rating = rating;
        self.age = age;
        self.is_online = is_online;

    def get_name(self):
        return self.name;
    def get_age(self):
        return self.age;
    def get_rating(self):
        return self.rating;
    def get_salutation(self):
        return self.salutation;
    def get_online(self):
        return self.is_online;
    def get_chats(self):
        return self.chats;
    def clear_chats(self):
        self.chats=[];