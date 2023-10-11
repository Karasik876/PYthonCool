n  = [int(x) for x in open('input.txt')]
for i in range(len(n)):
    N = n[i]
    sqr_num = int(N**0.5) #номер квадрата, в котором мы находимся
    flag_chetn = 0 #флаг четности показывает "идём" мы по четному квадрату или по нечетному

    if sqr_num % 2 != 0:
        ver = [-(sqr_num//2+1), sqr_num//2] #"вершина" - место, где начинается n квадрат
    else:
        flag_chetn = 1 #вершина четная
        ver = [sqr_num//2, -sqr_num//2] #"вершина" - место, где начинается n квадрат

    steps = N - sqr_num**2 #количество шагов, которые необходимо совершить по квадрату до перехода на следующий

    if flag_chetn: #если квадрат чётный, то мы сначала идём вверх на sqr_num шагов, потом идём влево, если steps>sqr_num
        if steps <= sqr_num:
            res = [ver[0], ver[1]+steps]
        else:
            res = [ver[0] - steps + sqr_num, ver[1] + sqr_num]
    else: #если квадрат нечётный, то мы идём вниз на sqr_num шагов, потом идём влево, если steps>sqr_num
        if steps <= sqr_num:
            res = [ver[0], ver[1]-steps]
        else:
            res = [ver[0] + steps - sqr_num, ver[1]-sqr_num]
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write(str(res[0]) + ' ' + str(res[1]) + "\n")
