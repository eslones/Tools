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

try:
  alvo = input('\nDigite link do site ([exemplo] https://www.youtube.com): ')

  wordlist = input('\nQual o nome da wordlist que você deseja usar? ([exemplo] miniwordlist.txt): ')

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
except:
  print('Erro... revise o link ou a wordlist e certifique que estão corretos')
 


