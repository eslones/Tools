#By:Eslones

import requests
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')


print('                                ')
print('  _____     __           _   _  ')
print(' |  __ \   / _|         (_) | | ')
print(' | |  | | | |_    __ _   _  | | ')
print(' | |  | | |  _|  / _` | | | | | ')
print(' | |__| | | |   | (_| | | | | | ')
print(' |_____/  |_|    \____| |_| |_| ')
print('                                ')
print('Precisa de ajuda? entre no laboratorio do nosso servidor: https://discord.gg/7dwt9qHnmy')


alvo = input('\nQual site voce quer buscar os dominios?:\t')

wordlist = input('\nQual wordlist voce vai usar?:\t')

wordlist_escolha = open(wordlist)

linha = wordlist_escolha.readline()

print('\n')

for linha in wordlist_escolha:
  
  requeste = requests.get(alvo+'/'+linha)

  code = requeste.status_code
  
  if code == 200:
    
    print(f'[ON] ==> {alvo}/{linha}', end="")
  else:
    print(f'[OFF] -- {alvo}/{linha}', end="")



