from pymongo import MongoClient

CLIENT = MongoClient()
DB = CLIENT.DB
PASS_DB = DB.PASS_DB

PASS_DB.drop()


class MyFuckingTime:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutess
    def __add__(self,other):
        if self.minutes+other.minutes >= 60:
            if self.hours + other.hours + 1 > 24:
                raise ValueError("Go sleep, faggot")
            return MyFuckingTime(self.hours + other.hours + 1, self.minutes+other.minutes-60)
        else:
            if self.hours + other.hours > 24:
                raise ValueError("Go sleep, faggot")
            return MyFuckingTime(self.hours + other.hours, self.minutes+other.minutes)
    def __mul__(self, other):
        for i in range(other):
            self.minutes+=15
            if self.minutes >= 60:
                self.minutes = 0
                self.hours+=1
                if self.hours >= 24:
                    raise ValueError("Go sleep, faggot")
        return MyFuckingTime(self.hours, self.minutes)
    def __str__(self):
        time = str(self.hours) + ":" + str(self.minutes)
        return time

def estimate_time(labcount, time):
    time = time.split('.')
    time = MyFuckingTime(time[0], time[1])
    time = time*labcount
    return time


def create_kebab(surname, labcount, time):
    for value in range(labcount):
        cursor = PASS_DB.find({"time":time})
        if cursor.count() == 0:
            PASS_DB.insert_one({"Surname":surname, "Labs":labcount, "Start":time, "Finish":str(estimate_time(value, time))})
            time = estimate_time(value, time)
        else
            raise ValueError("U mad, bro?")
            return


def show_kebab(time):
    cursor = PASS_DB.find({"time":time})
    if cursor.count() == 0:
        return None
    else

    pass

def remove_kebab():
    pass
