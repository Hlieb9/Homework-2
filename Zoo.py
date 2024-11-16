class Animal:
    def __init__(self, name):
        self.__name = name

    def info(self):
        print("Name:", self.__name)


class Mammals(Animal):
    def move(self):
        print("I'm move")


class Fish(Animal):
    def swim(self):
        print("I'm swim")


class Cat(Mammals):
    def __init__(self, name, mouse):
        self.__mouse = mouse
        super().__init__(name)

    def info(self):
        super().info()
        print("Mouse: ", self.__mouse)

    def cathMouse(self):
        print("I'm catching a mouse")
        self.__mouse += 1


class Dog(Mammals):
    def __init__(self, name, art):
        self.__art = art
        super().__init__(name)

    def info(self):
        super().info()
        print("Art: ", self.__art)

    def makeart(self):
        print("I'm making art")
        self.__art += 1


class GoldenFish(Fish):
    def __init__(self, name, wishes):
        self.__wishes = wishes
        super().__init__(name)

    def info(self):
        super().info()
        print("Wishes left: ", self.__wishes)

    def swim(self):
        print("I swim")

    def makewishes(self):
        if self.__wishes > 0:
            print("Making a wish!")
            self.__wishes -= 1
        else:
            print("No wishes left!")

    def leftwishes(self):
        return self.__wishes



cat = Cat("Tom", 10)
cat.info()
cat.cathMouse()
cat.info()
cat.move()

dog = Dog("Muhtar", 6)
dog.makeart()
dog.info()

golden_fish = GoldenFish("Goldy", 3)
golden_fish.info()
golden_fish.makewishes()
golden_fish.makewishes()
golden_fish.info()