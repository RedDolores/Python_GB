class ChekInt:
    def __set_name__(self, owner, attr):
        self.attr = attr

    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('Должно быть число, введен другой тип данных')
        if value < 0:
            raise ValueError('Число должно быть положительным')
        instance.__dict__[self.attr] = value


class CheckStr:
    def __set_name__(self, owner, attr):
        self.attr = attr

    def __set__(self, instance, value):
        if type(value) is not str:
            raise ValueError('Должна быть строка, введен другой тип данных')
        instance.__dict__[self.attr] = value


class Worker:
    wage = ChekInt()
    bonus = ChekInt()
    name = CheckStr()
    surname = CheckStr()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': int(self.wage), 'bonus': int(self.bonus)}


class Position(Worker):

    def __str__(self):
        return f'{self.get_full_name()} {self.position} ' \
               f'{self.get_total_income()}'

    def get_full_name(self):
        self.full_name = f'{self.name} {self.surname}'
        return self.full_name

    def get_total_income(self):
        self.total_income = self._income.get('wage') + \
                            self._income.get('bonus')
        return self.total_income


b = Position('Ivan', 'Ivanov', 'manager', 10, 20)
print(b.name)
print(b.position)
print(b.get_full_name())
print(b.get_total_income())
print(b)
