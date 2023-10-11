n = int(input())
print('Неверный ввод' if n < 0 else ' 1'.join([bin(n)[2:], oct(n)[2:], hex(n)[2:]]))