class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} is being fed")

class Cow(Animal):
    def milk(self):
        print(f"{self.name} is being milked")

class Sheep(Animal):
    def shear(self):
        print(f"{self.name} is being sheared")

class Chicken(Animal):
    def collect_eggs(self):
        print(f"{self.name} is laying eggs")

class Duck(Animal):
    def collect_eggs(self):
        print(f"{self.name} is laying eggs")

class Goose(Animal):
    def collect_eggs(self):
        print(f"{self.name} is laying eggs")

# Создаем экземпляры классов для каждого животного
seriy_goose = Goose("Серый", 5)
bely_goose = Goose("Белый", 4)
manka_cow = Cow("Манька", 300)
barashek_sheep = Sheep("Барашек", 50)
kudryavy_sheep = Sheep("Кудрявый", 55)
ko_ko_chicken = Chicken("Ко-Ко", 2)
kukareku_chicken = Chicken("Кукареку", 2)
roga_goat = Sheep("Рога", 40)
kopyta_goat = Sheep("Копыта", 38)
kryakva_duck = Duck("Кряква", 4)

# Список всех животных
animals = [seriy_goose, bely_goose, manka_cow, barashek_sheep, kudryavy_sheep, ko_ko_chicken, kukareku_chicken, roga_goat, kopyta_goat, kryakva_duck]

# Взаимодействие с животными
for animal in animals:
    animal.feed()
    if isinstance(animal, Cow) or isinstance(animal, Sheep):
        print (animal.milk() or animal.shear())
    	
    if isinstance(animal, Chicken) or isinstance(animal, Duck) or isinstance(animal, Goose):
        animal.collect_eggs()

# Подсчет общего веса животных и вывод самого тяжелого животного
total_weight = sum(animal.weight for animal in animals)
heaviest_animal = max(animals, key=lambda animal: animal.weight)

print(f"Общий вес всех животных: {total_weight} кг")
print(f"Самое тяжелое животное: {heaviest_animal.name} ({heaviest_animal.weight} кг)")
