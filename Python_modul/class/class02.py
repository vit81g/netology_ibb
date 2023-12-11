"""Родительский класс"""
class Hero():
    """объявляем атрибуты класса"""
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.rase = race
        self.health = 100

    """Объявляем методы класса"""
    def show_hero(self):
        discription = (self.name + "Level is: " + str(self.level) + "Race is: " + self.rase + "Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        self.level += 1

    def move(self):
        print("Hero " + self.name + "start moving")

    """изменение постоянной переменной через инкапсуляцию"""
    def set_health(self, new_health):
        self.health = new_health


"""класс наследник Hero"""
class SuperHero(Hero):
    """объявляем атрибуты класса"""
    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    """Объявляем дополнительные методы класса наследника"""
    def makemagic(self):
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + "Level is: " + str(self.level) + "Race is: " + self.rase + "Health is: " + str(self.health) + "Magic: " + str(self.magic)).title()
        print(discription)

