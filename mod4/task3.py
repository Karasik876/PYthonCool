def evk(a, b):
    if b == 0:
        return a
    else:
        return evk(b, a % b)

print(evk(360, 600))
print(evk(224, 12))