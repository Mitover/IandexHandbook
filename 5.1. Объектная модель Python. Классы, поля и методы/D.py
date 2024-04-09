class Programmer:
    def __init__(self, name, profile):
        self.alltime = 0
        self.balance = 0
        self.name = name
        self.profile = profile
        self.coefficient = 0
        if self.profile == "Junior":
            self.coefficient = 10
        elif self.profile == "Middle":
            self.coefficient = 15
        elif self.profile == "Senior":
            self.coefficient = 20

    def work(self, time):
        self.alltime += time
        self.balance += self.coefficient * time

    def rise(self):
        if self.profile == "Junior":
            self.profile = "Middle"
            self.coefficient = 15
        elif self.profile == "Middle":
            self.profile = "Senior"
            self.coefficient = 20
        else:
            self.coefficient += 1

    def info(self):
        return f"{self.name} {self.alltime}ч. {self.balance}тгр."