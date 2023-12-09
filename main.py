filepath = "adventofcode1.txt"
f = open(filepath, "r")
suma_number = 0
for line in f:
    list = []
    for x in line:
        if x.isdigit():
            list.append(x)
    number = 10 * int(list[0]) + int(list[len(list) - 1])
    suma_number += number
    print(number)
print(f'Wynik {suma_number}')
