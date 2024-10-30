import random

import self


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 0
        self.alive = True
        self.energy = 50
        self.money = 20

    def study(self):
        if self.progress < 3:
            print("Я пішов навчатися")
            self.progress += 2
            self.energy -= 1
            self.gladness -= 1

    def sleep(self):
        if self.energy < 5:
            print("Я пішов спати")
            self.energy += 2
            self.gladness += 2

    def chill(self):
        if self.gladness < 10:
            print("Я пішов на вулицю с друзями")
            self.energy -= 2
            self.gladness += 3
            self.progress -= 1
            self.money -= 1

    def energy(self):
        pass

    def info(self):
        print(f"На сьогодні {self.name} має")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання : {self.progress}")
        print(f"Енергія : {self.energy}")
        print(f"Гроші : {self.money}")

    def work(self):
        if self.money < 10:
            print("я пішов працювати")
            self.money += 3
            self.energy -= 2
            self.gladness += 1


    def is_alive(self):
        if self.progress < 0:
            print(f"В мене в голові сміття, немає сенсу жити")
            self.alive = False
        if self.gladness < 0:
            print(f"в мене депресія")
            self.alive = False
        if self.progress > 100:
            print(f"Я такий розумний що досроково закінчив малу академію шаг")
            self.alive = False
        if self.energy < 0:
            print(f"я зовсім знесиленний")
            self.alive = False
        if self.money < 0:
            print(f"В мене немає чим платити за їжу та дім")
            self.alive = False
        if self.money > 100:
            print(f"Я дуже богатий")
            self.alive = False

    def live(self,day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.chill()
        elif rnd == 3:
            self.sleep()
        elif rnd == 4:
            self.work()
        self.info()
        self.is_alive()
        print()




st = Student("Vasya")
for d in range(1,366):
    if st.alive == False:
        break
    st.live(d)