"""
Инкапсуляция - объеденить данные, безопасность содержимого, доступ к
содержимому ограничен. Public. _private - доступ только внутри класса.
_protected - доступ только внутри класса
В python это плохо реализовано
"""

"""Родительский класс"""

class Person():
      def __init__(self, name, gender, height=0, weight=0, hands=2):
          self.name = name
          self.gender = gender
          self.height = height
          self.weight = weight
          self.weapons = []     # будем присваивать пустой список для каждого экземпляра
          self.hands = hands
          self.alias = 'No alias'

      def eat(self, food):
          self.weight += food

      def do_exercise(self, hours):
          self.weight -= hours * 0.2

      def change_alias(self, new_alias):
          self.alias = new_alias

      def beat_up(self, foe):
          if not isintance(foe, Person):    #insintance проверка является ли объект экземпляром указанным
             return
          foe.status = 'defeated'
          self.status = 'winner'

peter = Person('Guru', 'Man', 180, 80)
print(peter.alias)
peter.change_alias('Furu')
print(peter.alias)
ivan = Person('ivan', 'man', 150, 60)
ivan.weapons = 'sword'
print(ivan.weapons)
print(peter.weapons)
print(peter.__dict__)         #покажет атрибуты экземпляра в виде словаря
