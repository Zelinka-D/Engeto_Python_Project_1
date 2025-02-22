"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dominik Zelinka
email: Dominik.Zelinka09@gmail.com
"""

# THE text
'''
author =
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Needed later for removing punctuation
import string

# Just simple text formatting, nothing fancy here..
class color:
    BOLD = '\033[1m'
    BLUE = '\033[94m'
    RED = '\033[91m' 
    END = '\033[0m'

num_texts = len(TEXTS)

# Function for visual formatting and saving my sanity
def vis():
    print("-" * 40)

# Function statistics for working with 'TEXTS'
def statistics():
    TEXTS_INPUT = TEXTS[int(num_selection) - 1]

    # Count of words
    word_count = len(TEXTS_INPUT.split())
    print(f"There are {word_count} words in the selected text.")

    #C ount of titlecase words
    title_count = TEXTS_INPUT.split()
    title_count_final = sum(1 for t_count in title_count if t_count.istitle())
    print(f"There are {title_count_final} titlecase words.")

       # Count of uppercase words
    upper_count = TEXTS_INPUT.split()
    upper_count_final = sum(1 for up_count in upper_count if up_count.isupper() and up_count.isalpha())
    print(f"There are {upper_count_final} uppercase words.")

       # Count of lowercase words
    lower_count = TEXTS_INPUT.split()
    lower_count_final = sum(1 for low_count in lower_count if low_count.islower())
    print(f"There are {lower_count_final} lowercase words.")

       # Count of numeric strings
    numeric_count = TEXTS_INPUT.split()
    numeric_count_final = sum(1 for num_count in numeric_count if num_count.isnumeric())
    print(f"There are {numeric_count_final} numeric strings.")

       # Count of summary of all numbers in TEXTS
    sum_count = TEXTS_INPUT.split()
    sum_count_final = sum(int(summary) for summary in sum_count if summary.isnumeric())
    print(f"The sum of all the numbers is {sum_count_final}.")

    vis()
    
# List of registered users
reg_user = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}


# Log-in inputs
log_name = input("\n" + color.BOLD + "Enter your username: " + color.END)
log_passw = input(color.BOLD + "Enter your password: " + color.END)
vis()


# Checking log-in name and password
if log_name in reg_user and log_passw == reg_user[log_name]:
    print("Welcome to the app,", color.BOLD + color.BLUE + (log_name) + color.END)
    print(f"We have {num_texts} texts to be analyzed.")
    vis()
else:
    print(color.RED + "Unregistered user, terminating the program.." + color.END)
    quit()

# Cycle to filter out wrong input and calls function 'statistics', also no more colors, got bored of it.
while True:
       selection = (input(f"Enter a number btw. 1 and {num_texts} to select: "))

       if not selection.isdigit():
             print(f"Invalid input, please try again. Input must be between 1 and {num_texts}..")
       else:
            selection = int(selection)

            if selection in range(1, 4):
                print("-" * 40)
                num_selection = int(selection)
                statistics()
                break   
            else:
                print(f"Invalid input, please try again. Input must be between 1 and {num_texts}..")


# Replacing shady punctuation
OCCURENCES_count = TEXTS[int(num_selection) - 1].replace(",", " ").replace(".", " ").split()

# Adding lenghts of words to list
OCCURENCES_length_words = [len(occu_count) for occu_count in OCCURENCES_count]

# Adding lenghts of words to dictionary, so i can keep track amount of each word lenght // next time I'll choose better names..
OCCURENCES_length_dict = {}
for occu_length in OCCURENCES_length_words :
    if occu_length in OCCURENCES_length_dict:
        OCCURENCES_length_dict[occu_length] += 1
    else:
        OCCURENCES_length_dict[occu_length] = 1
        


# Finally, the bar graph
print("LEN|     OCCURENCES    |NR.")
vis()
for OCCURENCES_count in sorted(OCCURENCES_length_dict):
    print(f"{OCCURENCES_count:3}|{'*' * OCCURENCES_length_dict[OCCURENCES_count]:18} |{OCCURENCES_length_dict[OCCURENCES_count]}")