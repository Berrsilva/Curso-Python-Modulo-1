text = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(text))
print('Só tem espaços? ', text.isspace())
print('É um número? ', text.isnumeric())
print('É alfabetico? ', text.isalpha())
print('É alfanumérico? ', text.isalnum())
print('Está em maiusculo? ', text.isupper())
print('Está em minisculo?', text.islower())
print('Está capitalizado? ', text.istitle())

if text.isalpha() == False:
    print('O texto não pode conter numero')
