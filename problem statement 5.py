
import re

text = "My email is student@gmail.com"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.search(pattern, text)

if result:
    print("Email found:", result.group())
else:
    print("Email not found")
