from pathlib import Path
import re

""" Funkcja generująca możliwe konfiguracje sprężyn:
    1. Definicja atrybutów pomocniczych.
    2. Iterowanie kondycji każdego elementu sprężyny.
    3. Iterowanie prawdobnych kombinacji po ostatnich wynikach sprężyn.
    4. Ograniczenie do niewiadomych elementów.
    5. Generowanie elementu zepsutego albo sprawnego z ograniczeniem do ilości zepsutych elementów.
    6. Dodawanie elementów do listy możliwości.
"""


def generate_combinations(combinations_list1, sum1):
    results = ['']

    for condition in combinations_list1:
        new_results = []
        for combination in results:
            if condition == '?':
                if len(combination) < len(combinations_list1):
                    if combination.count('#') < sum1:
                        new_results.append(combination + '#')
                    new_results.append(combination + '.')
            else:
                new_results.append(combination + condition)
        results = new_results

    return results


""" Funkcja przesiewająca rozwiązania:
    1. Definicja atrybutów pomocniczych.
    2. Iteracja sprężyn z listy sprężyn.
    3. Iteracja każdego elementu sprężyny.
    4. Tworzenie listy kombinacji dla sprawdzanej sprężyny.
    5. Sprawdzenie czy kombinacja zgadza się z kombinacją wsadową.
    6. Tworzenie listy poprawnych kombinacji.
    7. Zliczanie poprawnej ilości kombinacji.
"""


def separate_combinations(springs_list1):
    counter = 0
    counter1 = 0
    combinations_list2 = []
    springs_list2 = []
    for springs in springs_list1:
        for spring1 in springs:
            if spring1 == "#":
                counter += 1
                counter1 += 1
            else:
                if counter > 0:
                    combinations_list2.append(counter)
                counter = 0
        if counter > 0:
            combinations_list2.append(counter)
        if combinations_list2 == combinations_list and sum == counter1 and combinations_list[::-1] == combinations_list2[::-1]:
            springs_list2.append(springs)
            counter = 0
            counter1 = 0
            combinations_list2.clear()
        else:
            counter = 0
            counter1 = 0
            combinations_list2.clear()
    return len(springs_list2)

# Atrybuty pomocnicze
combinations_list = []
spring = []
sum = 0
springs_list = [[]]
good_counter = 0
number_pattern = re.compile(r'\d+')

# Wczytywanie pliku wejściowego
advent_txt = Path(__file__).parent / "adventofcode12.txt"
input_value = open(advent_txt).readlines()

# Funkcja główna
for input1 in input_value:

# Generowanie sprężyny wsadowej.
    for i in input1:
        if i == "?" or i == "#" or i == ".":
            spring.append(i)
# Generowanie kombinacji wsadowej oraz sumy zepsutych elementów sprężyny.
    numbers = number_pattern.findall(input1)
    for number in numbers:
        num = int(number)
        combinations_list.append(num)
        sum += num
# Generowanie listy potencjalnych sprężyn.
    springs_list = generate_combinations(spring, sum)
    spring.clear()
# Zliczanie poprawych kombinacji
    good = separate_combinations(springs_list)
    good_counter += good
    combinations_list.clear()
    springs_list.clear()
    sum = 0

print(good_counter)
