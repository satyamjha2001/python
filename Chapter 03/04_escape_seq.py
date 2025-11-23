# Python Escape Sequence Characters Examples

# Original example
a = 'Satyam is a good boy\nbut not a bad \'boy\''
print("Original example:")
print(a)

print("\n" + "="*50)
print("COMPREHENSIVE ESCAPE SEQUENCES EXAMPLES")
print("="*50)

# 1. Newline (\n)
print("\n1. Newline (\\n):")
text1 = "First line\nSecond line\nThird line"
print(text1)

# 2. Tab (\t)
print("\n2. Tab (\\t):")
text2 = "Name:\tJohn\nAge:\t25\nCity:\tNew York"
print(text2)

# 3. Backslash (\\)
print("\n3. Backslash (\\\\):")
text3 = "This is a backslash: \\ and this is a path: C:\\Users\\Documents"
print(text3)

# 4. Single quote (\')
print("\n4. Single quote (\\'):")
text4 = 'I can\'t believe it\'s working!'
print(text4)

# 5. Double quote (\")
print("\n5. Double quote (\\\"):")
text5 = "He said \"Hello World\" to everyone"
print(text5)

# 6. Carriage return (\r)
print("\n6. Carriage return (\\r):")
print("Hello\rWorld")  # World overwrites Hello
print("Loading...\rComplete!")  # Complete! overwrites Loading...

# 7. Backspace (\b)
print("\n7. Backspace (\\b):")
text7 = "Hello\b World"
print(text7)

# 8. Form feed (\f)
print("\n8. Form feed (\\f):")
text8 = "Page 1\fPage 2"
print(repr(text8))  # Using repr to show the escape character

# 9. Vertical tab (\v)
print("\n9. Vertical tab (\\v):")
text9 = "Line 1\vLine 2"
print(repr(text9))

# 10. Null character (\0)
print("\n10. Null character (\\0):")
text10 = "Hello\0World"
print(repr(text10))

# 11. Octal notation (\ooo)
print("\n11. Octal notation (\\ooo):")
text11 = "\101\102\103"  # A, B, C in octal
print(f"Octal \\101\\102\\103 = {text11}")

# 12. Hexadecimal notation (\xhh)
print("\n12. Hexadecimal notation (\\xhh):")
text12 = "\x41\x42\x43"  # A, B, C in hexadecimal
print(f"Hex \\x41\\x42\\x43 = {text12}")

# 13. Unicode notation (\uxxxx and \Uxxxxxxxx)
print("\n13. Unicode notation:")
text13a = "\u0041\u0042\u0043"  # A, B, C in unicode
text13b = "\u2764"  # Heart symbol
text13c = "\U0001F600"  # Grinning face emoji
print(f"Unicode \\u0041\\u0042\\u0043 = {text13a}")
print(f"Unicode \\u2764 = {text13b}")
print(f"Unicode \\U0001F600 = {text13c}")

# Raw strings (r"") - ignores escape sequences
print("\n14. Raw strings (prefix with r):")
raw_string = r"This is a raw string\nNo newline here\tNo tab here"
print(f"Raw string: {raw_string}")
normal_string = "This is a normal string\nNewline here\tTab here"
print(f"Normal string: {normal_string}")

# Practical examples
print("\n" + "="*50)
print("PRACTICAL EXAMPLES")
print("="*50)

# File paths (Windows)
print("\n1. File paths:")
file_path = "C:\\Users\\Documents\\file.txt"
print(f"Windows path: {file_path}")

# JSON-like string
print("\n2. JSON-like string:")
json_like = "{\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}"
print(f"JSON: {json_like}")

# Multi-line string with proper formatting
print("\n3. Multi-line formatted text:")
formatted_text = """Name:\tJohn Doe
Age:\t25
Email:\tjohn@example.com
Address:\t123 Main St,
\t\tNew York, NY"""
print(formatted_text)

# Combining multiple escape sequences
print("\n4. Complex example:")
complex_example = "Hello\tWorld!\nThis is a \"quoted\" text with \'single quotes\' too.\nPath: C:\\Users\\Documents\\file.txt\nEnd of example."
print(complex_example)