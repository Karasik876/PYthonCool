import re

def check_color(color):
    """
    Функция осуществляет проверку, может ли являться входная строка (целиком) корректной записью цвета в одном из трёх web форматов rgb, hex или hsl.

    Args:
    color (str): Строка для проверки.

    Returns:
    bool: True, если строка соответствует критериям, False - если нет.

    Examples:
    >>> check_color('#21f48D')
    True

    >>> check_color('#888')
    True

    >>> check_color('rgb(255, 255,255)')
    True

    >>> check_color('rgb(10%, 20%, 0%)')
    True

    >>> check_color('rgb(111%, 20%, 0%)') #проверка на выход за рамки 100% для rgb цвета
    False

    >>> check_color('hsl(200,100%,50%)')
    True

    >>> check_color('hsl(0, 0%, 0%)')
    True

    >>> check_color('#2345')
    False

    >>> check_color('ffffff')
    False

    >>> check_color('rgb(257, 50, 10)')
    False

    >>> check_color('hsl(20, 10, 0.5)')
    False

    >>> check_color('hsl(34%, 20%, 50%)')
    False
    """
    rgb_pattern = r'^rgb\(\s*((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*,\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*,\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]))\)$'
    rgb_percent_pattern = r'^rgb\(\s*((\d{1,2}|100)%\s*,\s*(\d{1,2}|100)%\s*,\s*(\d{1,2}|100)%)\)$'
    hex_pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    hsl_pattern = r'^hsl\(\s*(\d{1,3}|[0-9]{1,2}|[0-9]{1,2}\.\d{1,2})\s*,\s*((\d{1,2}|100)%)\s*,\s*((\d{1,2}|100)%)\s*\)$'

    return bool(re.match(rgb_pattern + '|' + rgb_percent_pattern + '|' + hex_pattern + '|' + hsl_pattern, color))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
