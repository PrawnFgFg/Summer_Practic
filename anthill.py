import asyncio
from bugs import *
class Anthill:
    def __init__(self):
        self.birth_place = []
        self.place_for_eggs = 1000
        self.num_larva = 0
        self.lvl_anthill = 1

        self.num_mushroom = 0
        self.num_aphid = 0
        self.num_food = 5000

        self.arr_NannyAnt = []
        self.arr_MaleAnt = []
        self.arr_SoldierAnt = []
        self.arr_WorkerAnt = []
        self.all_ants = 0

        self.count_for_timer = 0
        self.timer_attack = 30

    async def defence_from_bugs(self, arm_of_bugs, lable1, lable_amount_aphid, lable_amount_mushroom, show_results,
                                lable_attack, lable_def_attack2):
        count_attack = 0
        while True:
            await asyncio.sleep(1)

            if self.timer_attack > 0:
                self.timer_attack -= 1
                lable_attack["text"] = self.timer_attack
                lable_attack.update()
            if self.timer_attack == 0:
                count_attack += 1
                lable_def_attack2["text"] = str(count_attack)
                lable_def_attack2.update()

                lvl_bugs = arm_of_bugs.generate_bugs(anthill)

                if lvl_bugs < 450:
                    dead_ants = random.randint(230, 280)
                elif 650 <= lvl_bugs < 750:
                    dead_ants = random.randint(450, 613)
                else:
                    dead_ants = 701
                self.all_ants -= dead_ants

                dead_mushroom = self.num_mushroom // random.randint(2, 9)
                dead_aphid = self.num_aphid // random.randint(2, 3)

                lable_amount_mushroom["text"] = self.num_mushroom - dead_mushroom
                lable_amount_mushroom.update()

                lable_amount_aphid["text"] = self.num_aphid - dead_aphid
                lable_amount_aphid.update()

                show_results(dead_ants, dead_mushroom, dead_aphid)

                lable1.update()
                self.timer_attack = 30


    def distribution_worker_ants(self): # распределение рабочих муравьев
        ants = len(anthill.arr_WorkerAnt)
        dict_worker_ants = {}
        a1 = ants // 3
        a2 = (ants - a1) // 3
        a3 = ants - a1 - a2
        dict_worker_ants["GrAph"] = a2
        dict_worker_ants["GtrFoodAnt"] = a1
        dict_worker_ants["BuildAnt"] = a3
        return dict_worker_ants


    async def doing_ants_working(self, lable_amount_aphid, lable_count_food, lvl_ant_lable):
        while True:
            await asyncio.sleep(1)
            ants_dict = self.distribution_worker_ants()
            GrAph = ants_dict["GrAph"]
            # GtrFoodAnt = ants_dict['GtrFoodAnt']
            BuildAnt = ants_dict['BuildAnt']

            await asyncio.sleep(3)
            for ind, gr_ant in enumerate(self.arr_WorkerAnt):
                if ind == GrAph:
                    break
                gr_ant.grow_aphid(anthill)
                if self.num_aphid >= 1211:
                    self.num_aphid = 1211
                lable_amount_aphid["text"] = self.num_aphid
                lable_amount_aphid.update()

            await asyncio.sleep(2)
            for index, gr_food_ant in enumerate(self.arr_WorkerAnt):
                if GrAph < index < BuildAnt:
                    gr_food_ant.extract_food(anthill)
                    lable_count_food["text"] = self.num_food
                    lable_count_food.update()
                if index > BuildAnt:
                    break

            for i, build_ant in enumerate(self.arr_WorkerAnt):
                if i > BuildAnt:
                    build_ant.build_anthill(anthill)
                    if int(lvl_ant_lable["text"]) >= 80:
                        lvl_ant_lable["text"] = 80
                    else:
                        lvl_ant_lable["text"] = self.lvl_anthill // 500
                    lvl_ant_lable.update()

    async def collect_food_from_male(self):
        while True:
            await asyncio.sleep(5)
            for i in self.arr_MaleAnt:
                i.extract_food2(anthill)

    async def grow_lvl_from_soldier(self):
        while True:
            await asyncio.sleep(1)
            for i in self.arr_SoldierAnt:
                i.lvl_up_anthill(anthill)

    async def get_sugar(self, lvl_life_lable):
        while True:
            await asyncio.sleep(10)
            if self.num_aphid <= 300:
                lvl_life_lable["text"] = "low"
                lvl_life_lable["fg"] = "#800112"
            elif 300 < self.num_aphid <= 700:
                lvl_life_lable["text"] = "normal"
                lvl_life_lable["fg"] = "white"
            else:
                lvl_life_lable["text"] = "high"
                lvl_life_lable["fg"] = "#edc10e"
            lvl_life_lable.update()



    async def have_eating(self, lable_count_food):
        while True:
            await asyncio.sleep(5)
            if self.all_ants > 3000:
                self.num_food -= self.all_ants // 2
            else:
                self.num_food -= self.all_ants // 5
            if self.num_food <= 0:
                self.num_food = 0
            lable_count_food.update()
            lable_count_food["text"] = str(self.num_food)

    async def timer(self, time_of_life_lable): # количество прожитых дней муровейника
        while True:
            await asyncio.sleep(1)
            self.count_for_timer += 1
            time_of_life_lable["text"] = self.count_for_timer
            time_of_life_lable.update()


anthill = Anthill()