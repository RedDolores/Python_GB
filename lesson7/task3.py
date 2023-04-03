# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать публичные методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через
# перегрузку str str(self) - вызывается функциями str, print и format.
# Возвращает строковое представление объекта.

class Worker:

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
