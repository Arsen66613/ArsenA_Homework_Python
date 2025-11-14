class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst_name(self):
        print(self.first_name)

    def sayLast_name(self):
        print(self.last_name)

    def sayFull_name(self):
        print(self.first_name, self.last_name)


user = User('Имя', 'Фамилия')
user.sayFirst_name()
user.sayLast_name()
user.sayFull_name()
