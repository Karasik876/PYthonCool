alph = 'abcdefghijklmnopqrstuvwxyz'


a = ''
n = ''
v = str(input())
flag = 0

for i in range(len(v)):

    if v[i]==',':
        flag+=1
    if flag == 0:
        a+=v[i]
    elif flag == 1:
        flag += 1
        continue  #пропускаем одну итерацию, так как если этого не сделать, то переменная n будет начинаться с пробела
    elif flag == 2:
        n += v[i]


n = int(n)
c = 0

for i in alph:
    if a == i:
        break
    else:
        c+=1
print(alph[(c+n)%26])