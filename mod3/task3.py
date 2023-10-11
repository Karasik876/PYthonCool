n = str(input())
for j in [i for i in n.split('.')[::-1]]:
    print(j)