
import doctest

# Класс №1
class CreditCard:
    """ Созданиче и подготовка к работе объекта - кредитная карта"""
    def __init__(self, int_balance: (int, float), limit: (int, float),
                 operation_money: (int, float)):
        """
        :param int_balance: Исходный баланс кредитной карты
        :param limit: Допустимый лимит, позволяющий уходить "в минус"
        :param operation_mone: Сумма денежной операции с кредитной картой
                            (пополнение или снятие денежных средств)
        Пример:
        >>> Card_1 = CreditCard(5000, -1000, -3000) # инициализация экземпляра класса
        """
        if not isinstance(int_balance, (int, float)): #Проверка типа введенных данных
            raise TypeError
        self.balance = None
        self.init_balance(int_balance, operation_money)
        if not isinstance(limit, (int, float)): #Проверка типа введенных данных
            raise TypeError
        self.limit = limit
        if self.balance < self.limit: #Баланс кредитной карты не может быть меньше допустимого лимита
            raise ValueError
        if not isinstance(operation_money, (int, float)): #Проверка типа введенных данных
            raise TypeError
        self.operation_money = operation_money

    def init_balance(self, int_balance, operation_money):
        """ Функция для представления актуального баланса кредитной карты
        после совршения банковской операции """

        self.balance = int_balance + operation_money
        return self.balance

    def __str__(self) -> str:
        """ Функция для предоставления полной информации о кредитной карте
        после совершения банковской операции """
        return (f'Баланс карты после операции: {self.balance}, '
                f'Лимит:{self.limit} Сумма операции:{self.operation_money}')
"""
Примеры:
>>> Card_1 = CreditCard (3000, -500, 2000) # инициализация экземпляра класса
>>> Card_1.init_balance(5000, -4000) # инициализация экземпляра класса
"""

    # TODO работоспособность экземпляров класса проверить с помощью doctest
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


#Класс №2
class Vase:
    """ Созданиче и подготовка к работе объекта - ваза с цветами """
    def __init__(self, vase_volume: (int, float), water_volume: (int, float)):
        """
        :param vase_volume: Объем вазы с цветами
        :param water_volume: Объем воды в вазе

        Пример:
        >>> vase = Vase(800, 500) # инициализация экземпляра класса
        """
        if not isinstance(vase_volume, (int, float)): #Проверка типа введенных данных
            raise TypeError
        if vase_volume < 0: #Объем вазы не может принимать отрицательное значение
            raise ValueError
        self.vase_volume = vase_volume
        if not isinstance(water_volume, (int, float)): #Проверка типа введенных данных
            raise TypeError
        if water_volume < 0: #Объем воды не может принимать отрицательное значение
            raise ValueError
        self.water_volume = water_volume

    def empty_vase(self) -> bool:
        """
        Проверка есть ли в вазе с цветами вода
        :return: Есть ли вода в вазе

        Примеры:
        >>> vase = Vase(700, 0)
        >>> vase.empty_vase()
        """
        ...
    def add_water(self, volume_add_water: (int, float)):
        """
        Добавление воды в вазу с цветами
        :param volume_add_water: Объем добавляемой воды
        """

        if not isinstance(volume_add_water, (int, float)): #Проверка типа введенных данных
            raise TypeError
        if volume_add_water < 0: #Объем воды не может принимать отрицательное значение
            raise ValueError
        if volume_add_water > self.vase_volume: #Объем добавляемой воды не может превышать объем вазы
            raise ValueError
        ...

    def remove_water_vase(self, volume_extract_water: (int, float)):

        """
        Извлечение объема воды из вазы с цветами
        :param estimate_water: Объем извлекаемой воды
        """

        if not isinstance(volume_extract_water, (int, float)): #Проверка типа введенных данных
            raise TypeError
        if volume_extract_water < 0: #Объем воды не может принимать отрицательное значение
            raise ValueError
        if volume_extract_water > self.vase_volume: #Объем извлекаемой воды не может превышать объем вазы
            raise ValueError
        if volume_extract_water > self.water_volume: #Объем извлекаемой воды не может превышать объем воды в вазе
            raise ValueError

        """ 
        :return: Объем извлеченной жидкости
        
        Примеры:
        >>> vase = Vase(700, 500)
        >>> vase.remove_water_vase(400)
        """
        ...

#Класс №3
class Sofa:
    """ Созданиче и подготовка к работе объекта - диван """
    def __init__(self, length: (int, float), weight: (int, float), material: str, destination: str):
        """
        :param length: Длина дивана
        :param weight: Вес дивана
        :param material: Материал обивки дивана
        :param destination: Место нахождения дивана

        Пример:
        >>> sofa = Sofa(2800, 67, textile) # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):  # Проверка типа введенных данных
            raise TypeError
        if length < 0:  # Длина дивана не может принимать отрицательное значение
            raise ValueError
        self.length = length
        if not isinstance(weight, (int, float)):  # Проверка типа введенных данных
            raise TypeError
        if weight < 0:  # Вес дивана не может принимать отрицательное значение
            raise ValueError
        self.weight = weight
        if not isinstance(material, str):  # Проверка типа введенных данных
            raise TypeError
        self.material = material
        if not isinstance(destination, str):  # Проверка типа введенных данных
            raise TypeError
        self.destination = destination

    def move_object(self, new_destination: str) -> None:
        """ Перемещение дивана в новое место назначение """
        ...
    def research_comp_material(self) -> str:
        """ Исследование состава материала """
        ...
    def break_sofa(self, force: (int, float)) -> bool:
        """ Несущая способность дивана """
        if not isinstance(force, (int, float)):  # Проверка типа введенных данных
            raise TypeError
        """ 
        :param force: Сила, с которой давит приложенная нагрузка
        :return: ломается объект или нет
            
        Пример:
        >>> Sofa.break_sofa(150)
        """
        ...
