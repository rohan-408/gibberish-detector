import pandas as pd
import re

names_df = pd.read_csv('/Users/abc/Downloads/gibberish_data_classification_data.csv')  # path to names data file
# as we have many names in different formats such as emails, names with numbers, special characters, spaces etc. 
# the next obvious step would be to remove all these formating before we could compare it with our input string
name_list = list()
for i in names_df['input names']:
    i = str(i)
    # taking only usernames in case of emails
    if i.find('@')>=0:
        i = i.split('@')[0]
    i = re.sub(r'\d', '', i)  # Removing numbers from this string
    i = re.sub(r'[^a-zA-Z0-9]', '', i)  # Removing special characters from string
    i = i.lower()  # Converting this string to lowercase
    i = i.split(' ')
    for j in i:
        name_list.append(j)
def name_search(input_string):
    found =0
    for i in name_list:
        if i.find(input_string) >=0:  # searching every single name from our list with the input string
            found=1
            return found
        else:
            found =0
    return found