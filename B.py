import re

sentence = str(input())

match = re.findall(r'\Wkbtu|kbtu best|best kbtu|KBTU|KBTU best|best KBTU\W', sentence)

if match:
    print('Found a match')
else:
    print('Not matched')
