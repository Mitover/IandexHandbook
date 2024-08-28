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
###
class Programmer:

    def __init__(self, name, position) -> None:
        rank = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20
        }
        self.name = name
        self.wage = rank[position]
        self.work_time = 0
        self.salary = 0

    def work(self, time):
        self.work_time += time
        self.salary += self.wage * time

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'

    def rise(self):
        if self.wage < 20:
            self.wage += 5
        else:
            self.wage += 1
###
class Programmer:
    __rank = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.bonus = 0
        self.work_time = 0
        self.salary = 0

    def work(self, time):
        self.work_time += time
        self.salary += (self.__rank[self.position] + self.bonus) * time

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'

    def rise(self):
        match self.position:
            case 'Junior':
                self.position = 'Middle'
            case 'Middle':
                self.position = 'Senior'
            case 'Senior':
                self.bonus += 1
        # if self.position == "Junior":
        #     self.position= 10
        # elif self.position == "Middle":
        #     self.positiont = 15
        # elif self.position == "Senior":
        #     self.position = 20

        