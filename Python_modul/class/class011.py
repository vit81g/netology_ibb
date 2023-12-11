class Character:
      gender =''
      name = ''
      height = 0
      weight = 0
      hands = 2

# аргумент self ссылается на конкретный экземпляр класса. (который еще не создан)
# self обязательно надо прописывать, что бы показать то,
# что все действия будут проходить именно с тем объектом, к которому мы применяем метод

      def eat(self, food):
          self.weight += food

      def do_exercise (self, hours):
          self.weight -+ hours * 0.2

      def change_alias(self, new_alias):
          print(self) # смотрим для чего тут self
          self.alias = new_alias

      def printChar():
          print (self.gender, self.name, self.height, self.weight, self.hands)

bruce = Character()
bruce.name = 'Bruce Wayne'
bruce.height = 180
bruce.weight = 85
bruce.gender = 'man'

bruce.eat (2)
bruce.do_exercise(3)
bruce.change_alias('her')
