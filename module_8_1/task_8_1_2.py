"""
Класс: Транспорт
1. Скорость
2. Вместимость
3. Тип топлива
4. Расход топлива
    Методы:
        Заправка
        Движение
        Расход
"""

class Transport:
    def __init__(self, speed, capacity, fuel_type, fuel_consumption_per_100km):
        self.speed = speed
        self.capacity = capacity
        self.fuel_type = fuel_type
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_level = 0

    def refuel(self, amount):
        """Метод заправляет транспорт топливом."""
        self.fuel_level += amount
        return f"Транспорт заправлен на {amount} литров. Текущее количество топлива: {self.fuel_level} литров."

    def move(self, distance):
        """Метод моделирует движение транспорта на определенное расстояние."""
        fuel_needed = (distance / 100) * self.fuel_consumption_per_100km
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            return f"Транспорт движется на {distance} км со скоростью {self.speed} км/ч. Остаток топлива: {self.fuel_level} литров."
        else:
            return "Недостаточно топлива для движения!"

    def fuel_consumption(self, distance):
        """Метод рассчитывает расход топлива на заданное расстояние."""
        return (distance / 100) * self.fuel_consumption_per_100km


car = Transport(speed=120, capacity=5, fuel_type="Бензин", fuel_consumption_per_100km=8)
truck = Transport(speed=80, capacity=2, fuel_type="Дизель", fuel_consumption_per_100km=15)


print("\nМашина:")
print(car.refuel(50))
print(car.move(100))
print(f"Расход топлива на 100 км: {car.fuel_consumption(100)} литров.")
print()


print("\nГрузовик:")
truck.refuel(100)
truck.move(300)
print(f"Расход топлива на 300 км: {truck.fuel_consumption(300)} литров.")
