i_arr = [1, 2, 3, 4, 5, 3]

unique_i_arr = set(i_arr)

if len(unique_i_arr) == 1:
    print("Все числа равны")
elif len(unique_i_arr) == len(i_arr):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")