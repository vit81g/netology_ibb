"""отдельный файл python в котором описаны методы класса
   данный файл надо импортировать для включения класса в программу
   Class A и его параметры (атрибуты, методы) 
"""

class A():
    """родительский"""
    def __init__ (self, atr1, atr2, atr3):
        """атрибуты"""
        # объявляем параметры класса A 
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3
        self.atr4 = 100
    
    """ объявляем методы класса """
    def show_A(self):
        """печать атрибутов"""
        #discription = ("atr1: " self.atr1 + " atr2: " + self.atr2 + " atr3: " + self.atr3 + " atr4: " self.atr4)
        #discription = (self.atr1)
        discription = (f"art1: {self.atr1}; art2: {self.atr2}; art3: {self.atr3}; art4: {self.atr4}")
        print (discription)

    def func1(self):
        """повышение atr1"""
        self.atr1 += 1

    def func2(self):
        """повышение atr2"""
        print (self.atr2 + 1000)

    def set_atr4(self, new_atr4):
        """сброс постоянного атрибута art4 класса A"""
        self.atr4 = new_atr4
        print (f'{self.atr4}')
