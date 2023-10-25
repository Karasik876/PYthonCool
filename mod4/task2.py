
a = float(input("Введите число "))
n = int(input("Введите степень "))

def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return a * power(a, n - 1)



print(power(a, n))
