# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

script_name, first_param, second_param, third_param = argv


def wage(hours, rate_per_hour, bonus):
    print(hours * rate_per_hour + bonus)


wage(int(first_param), int(second_param), int(third_param))
