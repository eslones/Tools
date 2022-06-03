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


alvo = input('\nDigite link do site: ')

wordlist = input('\nQual nome da wordlist que voce deseja usar?: ')

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



