import re
sentence = str(input()).lower()
# pattern = str(r'ALMATY').lower()

match = re.findall(r'\balmaty\b', sentence)

result = list(match)

print(len(result))
