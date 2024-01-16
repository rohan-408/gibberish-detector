from name_search import *
import re
from letter_gap import *
from vowel_search import *
from unique_characters import *

input_string = str(input('Enter the text: '))
# removing numbers/ special characters or using only username as input
if input_string.find('@')>=0:  # taking only usernames in case of emails
    input_string = input_string.split('@')[0]
input_string = re.sub(r'\d', '', input_string)  # Removing numbers from this string
input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)  # Removing special characters from string
input_string = input_string.lower()  # Converting this string to lowercase

# Setting up conditions for gibberish/ non gibberish
output = list()  # variable for saving outputs for all individual formulas
output.append(name_search(input_string))  # name search
if calculate_average_distance(input_string) <= 3.7:  # Keyboard distance
    output.append(0)  # keeping the distance threshold as 3.7. below which considering as gibberish
else:
    output.append(1)
output.append(vowel_count(input_string))  # Vowel count
output.append(unique_chars(input_string))  # No. of unique characters

from collections import Counter
output_breakdown = Counter(output)
if output_breakdown[1]/(output_breakdown[1]+output_breakdown[0]) <= 0.5:  # if the overall score is less than equal to 50%, let's call this gibberish
    print("It's a Gibberish")
else:
    print("It's not a Gibberish")