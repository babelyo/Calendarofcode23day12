from pathlib import Path
import re


def generate_combinations(spring, sum1):
    """ Funkcja generująca możliwe konfiguracje łaźni gorąco-źródłowej.

        1. Definicja atrybutów pomocniczych.
        2. Iterowanie kondycji każdego elementu łaźni gorąco-źródłowe.
        3. Iterowanie prawdobnych kombinacji po ostatnich wynikach łaźnii gorąco-źródłowej.
        4. Ograniczenie do niewiadomych elementów.
        5. Generowanie elementu zepsutego albo sprawnego z ograniczeniem do ilości zepsutych elementów.
        6. Dodawanie elementów do listy możliwości.

        Args:
            spring: Lista elementów łaźni.
            sum1: Suma zepsutych elementów w łaźni.

        Returns:
            list: Lista możliwych łaźni.
    """

    results = ['']

    for condition in spring:
        new_results = []
        for combination in results:
            if condition == '?':
                if len(combination) < len(spring):
                    if combination.count('#') < sum1:
                        new_results.append(combination + '#')
                    new_results.append(combination + '.')
            else:
                new_results.append(combination + condition)
        results = new_results

    return results


def separate_combinations(springs_list, combinations_list, summary):
    """ Funkcja przesiewająca rozwiązania.

        1. Definicja atrybutów pomocniczych.
        2. Iteracja łaźni gorąco-źródłow z listy łaźni gorąco-źródłowy.
        3. Iteracja każdego elementu łaźni gorąco-źródłowej.
        4. Tworzenie listy kombinacji dla sprawdzanej łaźni gorąco-źródłowej.
        5. Sprawdzenie czy kombinacja zgadza się z kombinacją wsadową.
        6. Tworzenie listy poprawnych kombinacji.
        7. Zliczanie poprawnej ilości kombinacji.

        Args:
            springs_list: Lista możliwych łaźni.
            combinations_list: Lista poprawnej kombinacji zepsutych elementów łaźni.
            summary: Suma zepsutych elementów łaźni.

        Returns:
            int: Długość listy poprawnych łaźni.
    """

    counter = 0
    counter1 = 0
    combinations_list1 = []
    springs_list1 = []
    for springs in springs_list:
        for spring1 in springs:
            if spring1 == "#":
                counter += 1
                counter1 += 1
            else:
                if counter > 0:
                    combinations_list1.append(counter)
                counter = 0
        if counter > 0:
            combinations_list1.append(counter)
        if combinations_list1 == combinations_list and summary == counter1 and combinations_list[::-1] == combinations_list1[::-1]:
            springs_list1.append(springs)
            counter = 0
            counter1 = 0
            combinations_list1.clear()
        else:
            counter = 0
            counter1 = 0
            combinations_list1.clear()
    return len(springs_list1)


def parse_single_spring_input(input1):
    """ Generowanie łaźni gorąco-źródłowej wsadowej.

        Args:
            input1: Lista początkowa wszystkich łaźni
        Return:
            list: Lista elementów łaźni
    """
    return [i for i in input1 if i in ["?", "#", "."]]


def parse_broken_spring_groups(input1):
    """Generowanie kombinacji wsadowej oraz sumy zepsutych elementów łaźni gorąco-źródłowy.

        Args:
            input1: Lista początkowa wszystkich łaźni.
        Return:
            list: Lista poprawnej kombinacji zepsutych elementów łaźni.
            int: Suma zepsutych elementów łaźni.
    """
    combinations_list = []
    summary = 0
    number_pattern = re.compile(r'\d+')
    numbers = number_pattern.findall(input1)
    for number in numbers:
        num = int(number)
        combinations_list.append(num)
        summary += num
    return combinations_list, summary


def main():
    good_counter = 0

    advent_txt = Path(__file__).parent / "adventofcode12.txt"
    input_value = open(advent_txt).readlines()

    for input1 in input_value:
        spring = parse_single_spring_input(input1)
        combinations_list, summary = parse_broken_spring_groups(input1)
        springs_list = generate_combinations(spring, summary)
        spring.clear()
        good = separate_combinations(springs_list,  combinations_list, summary)
        good_counter += good
        combinations_list.clear()
        springs_list.clear()
    print(f'Suma wszystkich układów działających i uszkodzonych łaźni gorąco-źródłowy to {good_counter}. ')


if __name__ == "__main__":
    main()
