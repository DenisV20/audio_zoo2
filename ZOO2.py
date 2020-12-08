class Animals:
    # def __init__(self, name, voice, weight=0):
    #     self.name = name
    #     self.voice = voice
    #     self.weight = weight

    def eat(self):
        print('Животное ест')

    def sound(self):
        print('Животное кричит')


class Milk(Animals):
    def __init__(self, name, voice, weight=0):
        self.name = name
        self.voice = voice
        self.weight = weight


    def milking(self):
        print(self.name + ' подоена')

    # def quantity(self, liter):
    #     self.liter = liter
    #     print('У ' + self.name + ' было надоено ' + str(self.liter) + ' литр')


class Eggs(Animals):
    def __init__(self, name, voice, weight=0):
        self.name = name
        self.voice = voice
        self.weight = weight

    def collect(self):
        print('У ' + self.name + ' яйца собраны')

    # def quantity(self, eggs):
    #    self.eggs = eggs
    #    print('У ' + self.name + ' было собрано ' + str(self.eggs) + ' шт')


class Cut(Animals):
    def __init__(self, name, voice, weight=0):
        self.name = name
        self.voice = voice
        self.weight = weight

    def cutting(self):
        print(self.name + ' острижена')

    # def quantity(self, wool):
    #     self.wool = wool
    #     print('У ' + self.name + ' было собрано ' + str(self.wool) + ' кг')


class Cow(Milk):
    def quantity(self, liter):
        self.liter = liter
        return 'У ' + self.name + ' было надоено молока ' + str(self.liter) + ' литр'


class Goat(Milk):
    def quantity(self, liter):
        self.liter = liter
        return 'У ' + self.name + ' было надоено молока ' + str(self.liter) + ' литр'


class Geese(Eggs):
    def quantity(self, eggs):
        self.eggs = eggs
        return  'У ' + self.name + ' было собрано яиц ' + str(self.eggs) + ' шт'


class Chicken(Eggs):
    def quantity(self, eggs):
        self.eggs = eggs
        return  'У ' + self.name + ' было собрано яиц ' + str(self.eggs) + ' шт'


class Duck(Eggs):
    def quantity(self, eggs):
        self.eggs = eggs
        return 'У ' + self.name + ' было собрано яиц ' + str(self.eggs) + ' шт'


class Sheep(Cut):
    def quantity(self, wool):
        self.wool = wool
        return 'У ' + self.name + ' было собрано шерсти ' + str(self.wool) + ' кг'


cow = Cow('Манька', 'Му-Му', 350)
goat1 = Goat('Рога', 'Ме-Ме', 20)
goat2 = Goat('Копыта', 'Ме-Ме', 22)
geese1 = Geese('Grey', 'Шшшш', 13)
geese2 = Geese('White', 'Шшшш', 15)
chicken1 = Chicken('Ко-Ко', 'Ку-ка-ре-ку', 5)
chicken2 = Chicken('Кукареку', 'Ку-ка-ре-ку', 6)
duck = Duck('Кряква', 'Кря', 7)
sheep1 = Sheep('Барашек', 'Бее', 20)
sheep2 = Sheep('Кудрявый', 'Бее', 22)


print(goat1.voice)
print(cow.weight)
print(sheep2.name)
cow.quantity(2)
goat1.quantity(3)
goat2.quantity(2)
geese1.quantity(18)
geese2.quantity(2)
chicken1.quantity(20)
chicken2.quantity(4)
duck.quantity(4)
sheep1.quantity(1)
print(sheep2.quantity(2))

# duck.eat()


list_animals = [cow, goat1, goat2, geese1, geese2, chicken1, chicken2, duck, sheep1, sheep2]

for quantity_a in list_animals:
    print(quantity_a.quantity)






