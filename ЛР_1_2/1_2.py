
import doctest

class CreditCard:
    """ Созданиче и подготовка к работе объекта - кредитная карта"""
    def __init__(self, int_balance: (int, float), limit: (int, float),
                 operation_money: (int, float)):
    """
    :param int_balance: Исходный баланс кредитной карты
    :param limit: Допустимый лимит, позволяющий уходить "в минус"
    :param operation_mone: Сумма денежной операции с кредитной картой
                            (пополнение или снятие денежных средств
    Пример:
    >>> Card_1 = CreditCard(5000, -1000, -3000)
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


        self.balance = int_balance + operation_money
        return self.balance

    def __str__(self) -> str:
        return (f'Баланс карты после операции: {self.balance}, Лимит:{self.limit} Сумма операции:{self.operation_money}')

    # TODO работоспособность экземпляров класса проверить с помощью doctest
"""Примеры"""
Card_1 = CreditCard (3000, -500, 2000)
Card_1.init_balance(5000, -4000)

if __name__ == "__main__":
    doctest.testmod()


class Vase:
    def __init__(self, vase_volume: (int, float), water_volume: (int, float)):
        if not isinstance(vase_volume, (int, float)):
            raise TypeError
        if vase_volume < 0:
            raise ValueError
        self.vase_volume = vase_volume
        if not isinstance(water_volume, (int, float)):
            raise TypeError
        if water_volume < 0:
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

        if not isinstance(volume_add_water, (int, float)):
            raise TypeError
        if volume_add_water < 0:
            raise ValueError
        if volume_add_water > self.vase_volume:
            raise ValueError

    def remove_water_vase(self, volume_extract_water: (int, float)):

        """
        Извлечение объема воды из вазы с цветами
        :param estimate_water: Объем извлекаемой воды
        """

        if not isinstance(volume_extract_water, (int, float)):
            raise TypeError
        if volume_extract_water < 0:
            raise ValueError
        if volume_extract_water > self.vase_volume:
            raise ValueError

        """ 
        :raise ValueError: Если объем извлекаемой воды превышает объем воды в вазе с цветами, 
        то возвращается ошибка. 
        :return: Объем реально извлеченной жидкости
        
        Примеры:
        >>> vase = Vase(500, 500)
        >>> vase.remove_water_vase(400)
        """
        ...
