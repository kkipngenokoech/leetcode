class Multiverse:
    king = "King Julien"
    def sayHello(self):
        print ("Hello Multiverse!")
julien = Multiverse()
print (julien.king)
print(julien.sayHello())


# using __init__

class Multiverse:
    def __init__(self, king, personalAssistant):
        self.king = king
        self.personalAssistant = personalAssistant
    def meetTeam(self):
        print (f"{self.king} and {self.personalAssistant}")

madagascar = Multiverse("King Julien", "Maurice")
madagascar.meetTeam()


class Madagascar:
    crew = 0

    def __init__(self, name):
        self.name = name
        Madagascar.crew += 1
    def getCrew(self):
        print (f"{self.name}, crew number: {self.crew}")

Rico = Madagascar("Rico")
Rico.getCrew()
Kowalski = Madagascar("Kowalski")
Kowalski.getCrew()
Private = Madagascar("Private")
Private.getCrew()
Skipper = Madagascar("Skipper")
Skipper.getCrew()