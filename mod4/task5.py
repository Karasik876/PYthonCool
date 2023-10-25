
filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    text = file.read()

letters = {}
for char in text:
    letters[char] = letters.get(char,0) + 1

sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)

with open("output.txt", "w") as output_file:
    output_file.write("Буква\tКоличество\n")
    for letter, count in sorted_letters:
        output_file.write(f"{letter}\t{count}\n")