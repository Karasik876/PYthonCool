symbols = ['A', 'B', 'C', 'D', 'E']
def perevod(n, sis):
    result = ''
    while n:
        temp = n%sis
        if temp>9:
            temp = symbols[temp-10]
        result += str(temp)
        n//=sis
    return result[::-1]  #перворачиваем строку

v = float(input())

if int(v) == v: #исключаем дробные числа
    print(perevod(int(v), 2), perevod(int(v), 8), perevod(int(v), 16))
else:
    print('Неверный ввод')
