'''
A separate class User moduel

'''
class User():
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location

    def describe_user(self):
        user_info = {'first_name': self.first_name,
                     'last_name': self.last_name,
                     'age': self.age,
                     'gender': self.gender,
                     'location': self.location
                     }
        print(user_info)

    def greet_user(self):
        user_name = self.first_name + ' ' + self.last_name
        print('Hello %s, have a nice day!' % user_name)
