p = []
n = str(input())
p.append(n)

for i in range(len(n)-1):
    p.append(str(input()))

xc = ''
cx = ''
size = len(p[0])
flag_win = 0
for j in range(size): #проверяем победу по вертикали и горизонтали
    if flag_win:
        break 
    for k in range(size):
        xc += p[k][j] #все символы по вертикали
        cx += p[j][k] #все символы по горизонтали
        if xc.count('X')==size or cx.count('X')==size:
            print('X')
            flag_win += 1
            break
        elif xc.count('O')==size or cx.count('O')==size:
            print('O')
            flag_win += 1
            break
    xc = ''
    cx = ''

dx = ''
px = ''
if flag_win==0:
    for i in range(size): #проверяем победу по диагонали
        dx+=p[i][i]
        px+=p[i][size-i-1]
        if dx.count('X')==size or px.count('X')==size:
            print('X')
            flag_win+=1
            break
        elif dx.count('O')==size or px.count('O')==size:
            print('O')
            flag_win+=1
            break

if flag_win==0:
    print('Ничья')