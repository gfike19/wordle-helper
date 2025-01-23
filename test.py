import re

# Known letters and positions
first_letter = "a"
second_letter = "p"
fourth_letter = "l"

# Variable for the possible characters in unknown positions
possible_characters = "aeiou"  # Example: vowels

# Constructing the regex pattern
pattern = rf"^{first_letter}{second_letter}[{re.escape(possible_characters)}]{fourth_letter}[{re.escape(possible_characters)}]$"

print("pattern is ", pattern)



