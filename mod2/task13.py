
v = str(input())
sum = 0
for i in range(len(v)):
    if (i+1)%2!=0:
        sum += int(v[i])
    else:
        sum += 3 * int(v[i])
if sum%10==0:
    print('yes')
else:
    print('no')