import random

number = random.randint(1, 10)

attempts = 3

print("Спробуйте вгадати число від 1 до 10.")

for i in range(attempts):
    guess = int(input("Ваше число: "))
    if guess == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")
    if i == attempts - 1:
        print("Ви програли!")