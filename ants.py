import random
from anthill import anthill
import asyncio


class Ant:
    def __init__(self, status_ant):
        self.status_ant = status_ant

    def __repr__(self):
        return self.status_ant





class BigMomAnt(Ant):
    async def reproduction(self, anthill, male_ant):
        if male_ant:
            while True:
                await asyncio.sleep(2)
                eggs = random.randint(50, 200)
                if anthill.all_ants + eggs > 5000:
                    eggs = 5000 - anthill.all_ants

                anthill.place_for_eggs -= eggs
                anthill.num_larva += eggs


class MaleAnt(Ant):
    def extract_food2(self, anthill):
        anthill.num_food += 1

class NannyAnt(Ant):

    async def food_larva(self, anthill, lable_count_food):
        await asyncio.sleep(0.1)
        if anthill.num_larva > 0:
            all_food = 0
            for la in range(1, anthill.num_larva+1):
                food = random.randint(1, 10)
                if food <= 3:
                    anthill.arr_NannyAnt.append(NannyAnt("Няня_Муровей" + str(la)))
                elif food == 4:
                     anthill.arr_MaleAnt.append(MaleAnt("Муровей_Самец" + str(la)))
                elif food <= 6:
                    anthill.arr_SoldierAnt.append(SoldierAnt("Муровей_солдат" + str(la)))
                elif food >= 7:
                    anthill.arr_WorkerAnt.append(WorkerAnt("Рабочий_муровей" + str(la)))
                all_food += food
        anthill.num_food -= all_food
        if anthill.num_food <= 0:
            anthill.num_food = 0
        lable_count_food.update()
        lable_count_food["text"] = str(anthill.num_food)

    async def grow_mushroom(self, anthill, lable_amount_mushroom):
        while True:
            await asyncio.sleep(1)
            if anthill.num_food <= 5000:
                amount_gardeners = len(anthill.arr_NannyAnt) // 2
                anthill.num_mushroom += amount_gardeners
                if anthill.num_mushroom >= 1022:
                    anthill.num_mushroom = random.randint(777, 1011)
                lable_amount_mushroom["text"] = anthill.num_mushroom
                lable_amount_mushroom.update()

    async def collect_mushroom(self, anthill):
        while True:
            await asyncio.sleep(5)
            if anthill.num_mushroom > 0:
                if anthill.num_food <= 5000:
                    anthill.num_food += anthill.num_mushroom * 3
                    anthill.num_mushroom -= anthill.num_mushroom


class SoldierAnt(Ant):
    def lvl_up_anthill(self, anthill):
        anthill.lvl_anthill += 1


class WorkerAnt(Ant):

    def grow_aphid(self, anthill):
        anthill.num_aphid += 1

    def extract_food(self, anthill):
        anthill.num_food += random.randint(1, 2)

    def build_anthill(self, anthill):
        anthill.lvl_anthill += 1

class Larva:
    async def birth_ant(self, anthill, nanny_ant, lable1, all_ants_progress, lable_larva,
                        lable_count_food):
        while True:
            await asyncio.sleep(0.1)
            if anthill.num_larva > 0:
                anthill.all_ants += anthill.num_larva
                anthill.place_for_eggs = 1000
                await asyncio.sleep(1)
                await nanny_ant.food_larva(anthill, lable_count_food)

                anthill.num_larva -= anthill.num_larva

                lable_larva.update()
                lable_larva["text"] = str(anthill.num_larva) + "/ 1000"
                await asyncio.sleep(1)
                lable_larva["text"] = str(anthill.num_larva) + "/ 1000"
                lable_larva.update()


                lable1.update()
                lable1["text"] = str(anthill.all_ants) + "/ 5000"
                lable1.update()
                all_ants_progress["value"] = anthill.all_ants
                lable1.pack()



async def simulate(lab1, all_ants_progress, lable_larva, lable_count_food, lable_amount_mushroom, time_of_life_lable,
                   lable_amount_aphid, lvl_ant_lable, lvl_life_lable, arm_of_bugs, lable_attack, show_results,
                   lable_def_attack2):
    bg = BigMomAnt("Королева")
    larva = Larva()
    nanny_ant = NannyAnt("Няня")
    male_ant = MaleAnt('Самец')


    tasks = [asyncio.create_task(bg.reproduction(anthill, male_ant)),
             asyncio.create_task(larva.birth_ant(anthill, nanny_ant, lab1,
                                                 all_ants_progress, lable_larva, lable_count_food)),
             asyncio.create_task(anthill.timer(time_of_life_lable)), asyncio.create_task(nanny_ant.grow_mushroom(anthill, lable_amount_mushroom)),
             asyncio.create_task(nanny_ant.collect_mushroom(anthill)),
             asyncio.create_task(anthill.have_eating(lable_count_food)),
             asyncio.create_task(anthill.doing_ants_working(lable_amount_aphid, lable_count_food, lvl_ant_lable)),
             asyncio.create_task(anthill.get_sugar(lvl_life_lable)),
             asyncio.create_task(anthill.defence_from_bugs(arm_of_bugs, lab1, lable_amount_aphid, lable_amount_mushroom,
                                                           show_results, lable_attack, lable_def_attack2)),
             asyncio.create_task(anthill.collect_food_from_male()),
             asyncio.create_task(anthill.grow_lvl_from_soldier())]

    await asyncio.gather(*tasks)
    # await asyncio.sleep(140)

def start_asyncio(lab1, all_ants_progress, lable_larva, lable_count_food, lable_amount_mushroom, time_of_life_lable,
                  lable_amount_aphid, lvl_ant_lable, lvl_life_lable, arm_of_bugs, lable_attack, show_results,
                  lable_def_attack2):
    asyncio.run(simulate(lab1, all_ants_progress, lable_larva, lable_count_food, lable_amount_mushroom, time_of_life_lable,
                         lable_amount_aphid, lvl_ant_lable, lvl_life_lable, arm_of_bugs, lable_attack, show_results,
                         lable_def_attack2))



