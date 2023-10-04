s = ''
i = ''
v = str(input())
flag = 0

for k in range(len(v)):
    if v[k]==',':
        flag+=1
    if flag == 0:
        s+=v[k]
    elif flag == 1:
        flag += 1
        continue  #пропускаем одну итерацию, так как если этого не сделать, то переменная n будет начинаться с пробела
    elif flag == 2:
        i += v[k]

c = 0
for j in s:
    if i==j:
        c+=1
    else:
        break

print(c)