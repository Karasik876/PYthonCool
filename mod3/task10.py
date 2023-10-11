n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(j)
        else:
            print(j, end=', ')

print('')

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(i)
        else:
            print(i, end=', ')