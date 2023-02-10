class User: 

    active_users = 0 

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +- = 

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

user1 = User("Joe","Smith", 58)
user2 = User("Diane","Wang", 8)


print(user2.full_name())
print(user2.initials())