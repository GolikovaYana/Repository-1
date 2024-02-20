if __name__ == "__main__":
    # Write your solution here
    pass
class Car:
    """Базовый класс автомобили"""
    def __init__(self, model: str, power: int, year: int):

        """Атрибуты базового класса"""
        self.model = model #Модель машины
        self.power = power #Мощность машины
        self.year = year #Год выпуска машины

    def __str__(self) -> str:
        """Возвращает представление объекта в строчном виде"""
        return f"{self.model} мощностью {self.power}л.с. {self.year} года выпуска"

    def __repr__(self) -> str:
        """Возвращает параметры объекта"""
        return f"Car(model={self.model!r}, power={self.power!r}, year={self.year!r})"

    def start(self) -> str:
        """Метод для запуска двигателя"""
        return "Двигатель запущен"

class CombustionEngineCar(Car):
    """Дочерний класс - автомобили с ДВС"""
    def __init__(self, model: str, power: int, year: int, engine_type: str):

        """Атрибуты объекта CombustionEngineCar"""
        super().__init__(model, power, year)
        self.engine_type = engine_type #Тип двигателя (бензиновый, дизельный и т.д.)

    def start(self) -> str:
        """
        Перегруженный метод для запуска двигателя автомобиля с ДВС.

        В данном случае перегрузка метода позволяет добавить специфическое поведение при запуске двигателя
        автомобиля с ДВС, например, управление топливной системой или системой зажигания.

        """
        return f"Двигатель {self.engine_type} запущен"


class ElectricCar(Car):
    """Дочерний класс - электрокары"""
    def __init__(self, model: str, power: int, year: int, battery_capacity: float):
        """Атрибуты объекта ElectricCar"""
        super().__init__(model, power, year)
        self.battery_capacity = battery_capacity #Емкость батареи автомобиля (кВт⋅ч)

    # Метод start не перегружается, так как для электрокаров его поведение аналогично базовому классу Car.

    def __repr__(self) -> str:
        """Возвращает представление объекта ElectricCar"""
        return f"ElectricCar(model={self.model!r}, power={self.power!r}, year={self.year!r}, " \
               f"battery_capacity={self.battery_capacity!r})"