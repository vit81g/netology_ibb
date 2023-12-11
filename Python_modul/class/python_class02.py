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

class B(A):
    """класс нас наследник A, берет все особенности класса родителя"""
    # объявляем параметры класса B    
    def _init__(self, atr1, atr2, atr3, atr5):
        # наследуем атрибуты класса A (atr1, atr2, atr3) с помощью super().__init__
        super().__init__(atr1, atr2, atr3)
        self.atr5 = atr5 # объявляем новый параметр, отсутствующий в родительском классе
        self.atr6 = 200

    """ объявляем методы класса B"""
    def func3(self):
        """ уменьшение art5"""
        self.atr5 -= 10

    def show_A(self):
        """печать атрибутов"""
        discription = (f"art1: {self.atr1}; art2: {self.atr2}; art3: {self.atr3}; art4: {self.atr4}; atr5: {self.atr5}; atr6: {self.atr6}")
        print (discription)







