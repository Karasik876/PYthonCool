v = str(input())
result = ''
for i in range(len(v)):
    if v[i] == ' ':
        result+=v[i-1]
result += v[-1]
print(result)