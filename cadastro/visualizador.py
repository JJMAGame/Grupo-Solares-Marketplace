import csv

print("qual voce gostaria de ver os registro/dados?")
print("1. ver os dados de usuario")
print("2. ver os dados de orcamentos")
print("3. ver os dados de empresas")
print("4. Finalizar visualizador")

opcao_visualizador = int(input(""))
sair_visualizador = 1

while(sair_visualizador != 1):
 if(opcao_visualizador == 1):
  with open("cadastro/usuarios.csv", "r") as file:
    leitor = csv.reader(file, delimiter=';')
    for line in leitor:
      print(line)
  print("Quer visualizar outro arquivo?")
  opcao_visualizador = int(input(""))

 elif(opcao_visualizador == 2):
  with open("cadastro/orcamentos.csv", "r") as file:
    leitor = csv.reader(file, delimiter=';')
    for line in leitor:
      print(line)
  print("Quer visualizar outro arquivo?")
  opcao_visualizador = int(input(""))

 elif(opcao_visualizador == 3):
  with open("cadastro/empresas.csv", "r") as file:
    leitor = csv.reader(file, delimiter=';')
    for line in leitor:
      print(line)
  print("Quer visualizar outro arquivo?")
  opcao_visualizador = int(input(""))

 elif(opcao_visualizador == 4):
  sair_visualizador -= 1

 else:
  print("Opção inválida, por favor escolha uma opção válida")
  opcao_visualizador = int(input(""))