from importAgenda import heroes
from HeroAgenda import HeroAgenda

# Função para formatar texto com cores
def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Define o menu com cores
menu = f"""
    1 - {colorize("Adicionar super herói", "32")}
    2 - {colorize("Buscar super herói", "34")}
    3 - {colorize("Mostrar todos os super heróis", "33")}
    4 - {colorize("Remover super herói", "31")}
    5 - {colorize("Mostrar todos os super heróis pela primeira letra", "35")}
    6 - {colorize("Sair", "36")}
"""
heroAgenda = HeroAgenda()
for hero in heroes:
   heroAgenda.insert(hero)

while True:
  print('------------------')  
  print(menu)
  option = int(input("Escolha uma opção: "))
  if (option == 6):
     break
  elif (option == 1):
     hero = input("Insira o heroi: ")
     heroAgenda.insert(hero)
     print(hero + " adicionado")
  elif (option == 2):
     search = input("Insira o nome do heroi: ")
     print(heroAgenda.search(search))
  elif (option == 3):
    for hero in heroAgenda.table:
       if hero != None:
        if type(hero) != list:
           print(hero)
        else:
           for heroes in hero:
              print(heroes)
  elif (option == 4):
     hero = input("Insira o heroi que deseja remover: ")
     heroAgenda.removeItem(hero)
  elif (option == 5):
     char = input("Insira um caractere: ")
     print(heroAgenda.findByFirstChar(char))
  else:
     print("Invalid option")  