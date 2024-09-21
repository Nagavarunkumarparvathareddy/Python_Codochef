s = input().lower()
lst = list(s)
l = len(lst)
vowel = 0
blankspace = 0
for ele in lst:
    if ele =='a' or ele =='e' or ele == 'i' or ele == 'o' or ele == 'u':
        vowel += 1
    elif ele == ' ':
        blankspace += 1 
    else:pass
print('NO OF Vowels ',vowel)
print('No of consonants',l-(vowel+blankspace))
