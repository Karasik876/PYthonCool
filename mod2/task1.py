a = ''
b = ''
v = str(input())
flag = 0

for i in range(len(v)):
    if v[i]==',' or v[i]==' ':
        flag+=1
    if flag == 0:
        a+=v[i]
    elif flag == 2:
        flag+=1
        continue #пропускаем одну итерацию, так как если этого не сделать, то переменная b будет начинаться с пробела
    elif flag == 3:
        b+=v[i]
        print(b)

a = float(a)
b = float(b)

if int(a%b)==a%b:
    print(int(a%b))
else:
    print(a%b)