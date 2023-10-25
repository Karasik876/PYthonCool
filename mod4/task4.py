alph_d = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

def can_be_palindrome(word_letters):
    even = 0
    odd = 0
    for i in word_letters:
        if word_letters[i] != 0:
            if word_letters[i]%2==0:
                even+=1
            else: odd+=1
    if odd<=1:
        return True
    else:
        return False


a = str(input())

alph_d = {}
for char in a:
    alph_d[char] = alph_d.get(char, 0) + 1

result = ''
temp = ''
if can_be_palindrome(alph_d):
    for j in alph_d:
        if a.count(j)%2==0:
            result+=j*(a.count(j)//2) #составляем левую часть палиндрома
        else:
            temp+=j*a.count(j) #середина палиндрома с 'нечетной' буквой по середине
    temp2 = result[::-1]
    result = result + temp + temp2
    print(result)
else:
    print('Нельзя составить палиндром')



