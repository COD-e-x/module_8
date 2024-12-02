class Vehicle:
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage

    def get_vehicle_type(self, number_of_wheels):
        """Определяет тип транспортного средства по числу колес"""
        vehicle_types = {
            2: 'мотоцикл',
            3: 'трицикл',
            4: 'автомобиль'
        }

        if number_of_wheels not in vehicle_types:
            return f'Я не знаю таких ТС'

        vehicle_type = vehicle_types.get(number_of_wheels)
        return f'Это {vehicle_type} марки {self.brand}'

    def get_vehicle_advice(self):
        """Выдает совет покупателю опираясь на пробег"""
        if self.mileage < 0:
            return 'Пробег не может быть меньше 0'

        if self.mileage <= 50000:
            advice = 'можно брать.'
        elif self.mileage <= 100000:
            advice = 'надо внимательно проверить.'
        elif self.mileage <= 150000:
            advice = 'надо провести полную диагностику.'
        else:
            advice = 'лучше не покупать.'

        return f'{self.brand} {advice}'


yamaha = Vehicle('Yamaha', 40000)
print(yamaha.get_vehicle_type(1))
print(yamaha.get_vehicle_type(5))
print()
print(yamaha.get_vehicle_type(2))
print(yamaha.get_vehicle_advice())
print()

audi = Vehicle('Audi', 70000)
print(audi.get_vehicle_type(3))
print(audi.get_vehicle_advice())
print()

honda = Vehicle('Honda', 120000)
print(honda.get_vehicle_type(4))
print(honda.get_vehicle_advice())
print()

bmw = Vehicle('BMW', 160000)
print(bmw.get_vehicle_type(4))
print(bmw.get_vehicle_advice())
print()