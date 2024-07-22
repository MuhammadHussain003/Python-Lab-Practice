v=['a','e','i','o','u','A','E','I','O','U']

a=input("Enter a string: ")

vowel=0

for i in a:
    if i in v:
        vowel=vowel+1

print(vowel)