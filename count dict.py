#This code counts the occurence of the words in the sentence

text = input('Enter a text: ')

#To seprate sentence into words we introduce the block of code below

from string import punctuation
text = text.lower()
for p in punctuation:
    text = text.replace(p, '')
words = text.split()


d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1

items = list(d.items())
items.sort()
for i in items:
    print(i)