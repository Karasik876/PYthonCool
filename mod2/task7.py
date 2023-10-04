n = str(input())
odin = 0
nol = 0
for i in n:
    if i == "1":
        odin+=1
    else:
        nol+=1

if odin == nol:
    print('yes')
else:
    print('no')