# 14-m
class EmployeeSalary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase(self, percent):
        self.salary += self.salary * percent / 100

    def show_salary(self):
        print("Yangi oylik:", int(self.salary), "$")


e = EmployeeSalary("Ali", 1000)
e.increase(20)
e.show_salary()

# 15-m
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, damage):
        self.health -= damage
        print(self.name, "zarar oldi:", self.health, "HP qoldi")

    def heal(self, amount):
        self.health += amount
        print("Tiklandi:", self.health, "HP")


g = GameCharacter("Ali", 100)
g.attack(30)
g.heal(20)
