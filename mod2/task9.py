v = str(input())

gl = 'аеёиоуыэюя'
sogl = 'бвгджзйклмнпрстфхцчшщ'

def is_in(s, ar):
    for i in ar:
        if s == i:
            return True
    return False

gl_c = 0
sogl_c = 0

for i in v:
    if is_in(i, gl):
        gl_c+=1
    elif is_in(i, sogl):
        sogl_c+=1

print(gl_c, sogl_c)