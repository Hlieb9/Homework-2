score = int(input("Введіть кількість балів (0-100): "))

if 0 <= score <= 49:
    grade = "незадовільно"
elif 50 <= score <= 69:
    grade = "задовільно"
elif 70 <= score <= 89:
    grade = "добре"
elif 90 <= score <= 100:
    grade = "відмінно"

print(grade)