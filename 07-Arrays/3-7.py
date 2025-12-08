arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest_name=''
for word in arr:
    if len(word)>len(longest_name):
        longest_name=word
print(longest_name)
