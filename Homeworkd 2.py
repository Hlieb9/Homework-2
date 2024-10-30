class Dog:
    print("Hi!")
    count_of_dog = 0
    def __init__(self, name="No name", height=50, age=6, weight=10):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight

    def addYear(self):
        if self.age < 17:
            self.age += 1
        if self.age > 17:
            self.age += 1
        if self.age == 17:
            self.age += 1
        if self.age > 17:
            print(f"собачка вже померла, тому що дуже стара:(")

    def addWeight(self):
        if self.weight < 30:
            self.weight += 1
        if self.weight > 30:
            self.weight += 1
        if self.weight == 30:
            self.weight += 1
        if self.weight > 30:
            print(f"У собачки стався серцевий напад, тому що вона дуже важка і тому вона померла:(")

    def study(self):
        print("Я навчаюсь трюкам, гав гав!")

    def info(self):
        print(f"Name - {self.name}")
        print(f"Age - {self.age}")
        print(f"Height - {self.height}")
        print(f"Height - {self.weight}")

print(Dog.count_of_dog)

dog1 = Dog("Muhtar", 60, 6, 7)
dog1.addYear()
dog1.info()
print(dog1)

print(dog1.name)
print(dog1.height)
print(dog1.height)
print(dog1.age)
dog1.study()

dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.addYear()
print(dog1.age)