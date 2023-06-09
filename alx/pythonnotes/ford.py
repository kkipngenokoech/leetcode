class Ford:
    unique = 0000

    def __init__(self, name, year):
        self.name = name
        self.year = year
        Ford.unique += 1
    def getFord(self):
        print("Ford {}: unique {}".format(self.name, hex(self.unique)))

mustang = Ford("Mustang", 2022)
mustang.getFord()

explorer = Ford("Explorer", 2019)
explorer.getFord()

expedition = Ford("Expedition", 2017)
expedition.getFord()