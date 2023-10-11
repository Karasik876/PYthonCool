a = [int(a) for a in input().split()]
res = sum(a) - max(a) - min(a)
print(res)