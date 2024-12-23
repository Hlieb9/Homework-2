import random

class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        self.money += 40
        print("Я сьогодні працюю")

    def eat(self):
        self.house.food -= random.randint(1, 10)
        self.house.pollution += random.randint(1, 5)
        print("Я поїв")

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Я пішов в магазин пішки")
        else:
            if self.car.drive(random.randint(1, 10) * 10):
                print("Ми поїхали в магазин")
            else:
                print("Я пішов в магазин пішки")

    def chill(self):
        self.money -= random.randint(10, 20)
        self.house.pollution += random.randint(1, 5)
        print("Я гарно відпочив")

    def clean(self):
        if self.house.pollution > 0:
            cleaning_time = random.randint(1, 10)
            self.house.pollution -= cleaning_time
            if self.house.pollution < 0:
                self.house.pollution = 0
            print(f"Я прибрав в квартирі. Забруднення зменшилось на {cleaning_time}.")
        else:
            print("У мене вже чисто в квартирі!")

    def info(self):
        print(f"Гроші - $ {self.money}")
        print(self.house)
        if self.car != None:
            print(self.car)

    def live(self, day):
        print(f"День №{day}")
        choice = random.randint(1, 5)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()
        elif choice == 5:
            self.clean()

        if self.money > 1000:
            print("Купляємо авто!!!!")
            self.money -= 500
            self.car = Car("Sims car 12314")
        self.info()

        if self.house.pollution > 100:
            print("Забруднення перевищило 100! Симуляція завершена.")
            return False

        print()
        return True

    def is_alive(self):
        if self.money < 0:
            return False
        else:
            return True


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def add_food(self, food):
        if self.food + food <= 0:
            self.food += food
        else:
            self.food = 50

    def __str__(self):
        return f"Інформація про будинок: їжа - {self.food}, забруднення - {self.pollution}"


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60    # л
        self.state = 100  # %

    def drive(self, length):
        rashod = length * 0.1
        if self.fuel - rashod < 0:
            print("Подорож не можлива, не вистачає пального")
            return False
        else:
            print(f"Ми проїхали {length} км, втратили {rashod} л пального")
            self.fuel -= rashod
            self.state -= length * 0.01
            return True

    def add_fuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
        else:
            self.fuel = 60

    def __str__(self):
        return f"Авто {self.model}\nБензин - {self.fuel} л, стан - {int(self.state)} %"


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Професія: {self.name}, зарплатня - {self.salary}"


job = Job("Programmer", 1000)
human = Human("Anton", job=job)

for day in range(366):
    if not human.is_alive():
        break
    if not human.live(day):
        break