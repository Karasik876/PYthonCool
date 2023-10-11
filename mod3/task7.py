n = str(input())
print(True) if len([i for i in n.split(' ')]) == len(set([j for j in n.split(' ')])) else print(False)