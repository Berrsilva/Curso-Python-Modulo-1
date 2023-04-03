# utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como
# utilizar o código \033[m com todas as suas principais possibilidades.
print('\033[7;30;33mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
nome = 'Bernardo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
