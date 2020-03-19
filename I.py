def is_anagram(s, t):
    str(sorted(s))
    str(sorted(t))
    if str(sorted(s)) == str(sorted(t)):
        return True
    else:
        return False


s = str(input())
t = str(input())
if is_anagram(s, t):
    print('Anagram')
else:
    print('Not anagram')
