import random


class ArmyOfBugs:
    def __init__(self):
        self.crums = []
        self.spiders = []
        self.grasshopper = []


    def generate_bugs(self, anthill):
        if anthill.lvl_anthill < 10:
            num_crum = random.randint(50, 150)
            num_spider = random.randint(10, 20)
            num_grasshopper = random.randint(5, 10)

            for c in range(num_crum):
                self.crums.append(Crum())
            for s in range(num_spider):
                self.spiders.append(Spider())
            for g in range(num_grasshopper):
                self.grasshopper.append(Grasshopper())

        main_lvl_bugs = len(self.spiders) * 10 + len(self.grasshopper) * 20 + len(self.crums) * 3
        return main_lvl_bugs




class Bug:
    def __init__(self, identification):
        self.identification = identification
        self.lvl = 1


class Crum(Bug):
    def __init__(self, identification="Клоп"):
        super().__init__(identification)
        self.lvl = 3


class Spider(Bug):
    def __init__(self, identification="Паук"):
        super().__init__(identification)
        self.lvl = 10

class Grasshopper(Bug):
    def __init__(self, identification="Кузнечик"):
        super().__init__(identification)
        self.lvl = 20


arm = ArmyOfBugs()


