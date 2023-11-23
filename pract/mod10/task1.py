import re

def reg(s):
    """
    Проверяет соответствие переданной строки критериям корректности пароля

    Args:
    s (str): Строка для проверки.

    Returns:
    bool: True, если строка соответствует критериям, False - если нет.

    >>> p1 = 'rtG3FG!Tr^e'
    >>> reg(p1)
    True

    >>> p2 = 'aA1!*!1Aa'
    >>> reg(p2)
    True

    >>> p3 = 'oF^a1D@y5e6'
    >>> reg(p3)
    True

    >>> reg('пароль')
    False

    >>> reg('lOngPa$$$W0Rd')
    False

    >>> reg('PaSsw@o0#rd') #Подходящий пароль
    True

    >>> reg('Passw@o0!rd') #Не хватает заглавных букв
    False

    >>> reg('PaSsw@o!rd') #Не хватает цифр
    False

    >>> reg('PaSsw@o0rd') #Не хватает спец. символов
    False

    >>> reg('PaSsw@o0@rd') #2 одинаковых спец. символа
    False

    >>> reg('PaaaSsw@o0!rd') #3 подряд буквы 'a'
    False

    >>> p4 = 'enroi#$rkdeR#$092uWedchf34tguv394h'
    >>> reg(p4)
    True
    """
    return bool(re.match(r'^(?!.*([A-Za-z0-9^$%@#&*!?])\1\1)(?=(?:.*([$^%@#&*!?]).*(?!\2))([$^%@#&*!?]))(?=(?:.*[$^%@#&*!?]){2})(?=.*([$^%@#&*!?]))(?=([A-Za-z0-9^$%@#&*!?]*[A-Z]){2,})(?=([A-Za-z0-9^$%@#&*!?]*[0-9]+)).{6,}$', s, re.ASCII))



# запуск тестов
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # все тесты пройдены
