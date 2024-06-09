import re

# Sample input_value, you can replace it with your actual input
input_value = ["#???##?#???#?????.?? 17,1"]

# Initialize lists and sum
combinations_list = []
special_characters = []
total_sum = 0

# Define a regex pattern to find all numbers in the string
number_pattern = re.compile(r'\d+')

# Loop through each element in input_value
for input1 in input_value:
    # Find all numbers in the current string
    numbers = number_pattern.findall(input1)
    for number in numbers:
        num = int(number)
        combinations_list.append(num)
        total_sum += num

    # Find all special characters in the current string
    for char in input1:
        if char in ["?", "#", "."]:
            special_characters.append(char)

print("Combinations List:", combinations_list)
print("Special Characters List:", special_characters)
print("Sum of Numbers:", total_sum)