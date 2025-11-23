name = "satyam"
text = "  Hello World  "
sample_text = "Python Programming Language"

# Basic string functions
print("=== Basic String Functions ===")
print(f"Length of name: {len(name)}")
print(f"Ends with 'yam': {name.endswith('yam')}")
print(f"Starts with 'sa': {name.startswith('sa')}")
print(f"Capitalized: {name.capitalize()}")

# Case conversion functions
print("\n=== Case Conversion Functions ===")
print(f"Upper case: {name.upper()}")
print(f"Lower case: {name.lower()}")
print(f"Title case: {sample_text.title()}")
print(f"Swap case: {name.swapcase()}")

# String cleaning functions
print("\n=== String Cleaning Functions ===")
print(f"Strip whitespace: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# Search and replace functions
print("\n=== Search and Replace Functions ===")
print(f"Find 'tam': {name.find('tam')}")
print(f"Index of 'a': {name.index('a')}")
print(f"Count of 'a': {name.count('a')}")
print(f"Replace 'a' with 'o': {name.replace('a', 'o')}")

# String splitting and joining
print("\n=== Split and Join Functions ===")
words = sample_text.split()
print(f"Split into words: {words}")
print(f"Join with '-': {'-'.join(words)}")

# String validation functions
print("\n=== Validation Functions ===")
print(f"Is alphabetic: {name.isalpha()}")
print(f"Is numeric: {'123'.isdigit()}")
print(f"Is alphanumeric: {'abc123'.isalnum()}")
print(f"Is lowercase: {name.islower()}")
print(f"Is uppercase: {name.isupper()}")

# String formatting functions
print("\n=== Formatting Functions ===")
print(f"Center (20 chars): '{name.center(20, '*')}'")
print(f"Left justify: '{name.ljust(10, '-')}'")
print(f"Right justify: '{name.rjust(10, '-')}'")
print(f"Zero fill: {'42'.zfill(5)}")

# Advanced string functions
print("\n=== Advanced Functions ===")
multiline = "line1\nline2\nline3"
print(f"Split lines: {multiline.splitlines()}")
print(f"Partition: {sample_text.partition('Programming')}")
print(f"Starts with tuple: {name.startswith(('sa', 'ta', 'ya'))}")
print(f"Encode to bytes: {name.encode('utf-8')}")