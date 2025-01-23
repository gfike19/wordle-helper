import re

# Variable with the value to exclude
exclude_value = "example"

# Regex pattern to match strings that do NOT contain the value
pattern = rf"^(?!.*{re.escape(exclude_value)}).*"

# Test strings
strings = [
    "This is an example string.",
    "This string does not contain the keyword.",
    "Another example here.",
    "No matching word."
]

# Filtering strings that do not contain the exclude_value
filtered_strings = [s for s in strings if re.match(pattern, s)]

print(filtered_strings)

