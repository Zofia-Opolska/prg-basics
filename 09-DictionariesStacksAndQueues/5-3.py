translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
x=input('What ord would you like to translate? ')
if x not in translations:
    print('Translation is unavailable' )
else:
    print(f'The translation for word {x} is {translations[x]}')