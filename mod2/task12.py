v = str(input())
result = ''
allowed = "+1234567890"

def is_in(s, ar):
    for i in ar:
        if s == i:
            return True
    return False

for i in v:
    if is_in(i, allowed):
        result += i
print(result)