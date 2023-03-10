revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {revenue - costs}')
    print(f'Рентабельность выручки = {costs / revenue}')
    count_employees = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника = '
          f'{(revenue - costs) / count_employees}')
else:
    print(f'Финансовый результат - убыток. Его величина: {revenue - costs}')