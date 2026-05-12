import math
import empresas # Nota importante - para acessar a lista de empresas, é necessário importar o arquivo empresas.py, onde a lista de empresas está definida. Certifique-se de que o arquivo empresas.py esteja no mesmo diretório do arquivo Marketplace.py para que a importação funcione corretamente.

# Sessão de login
print("Ola Seja bem-vindo ao Grupo Solares Marketplaced")
nome = input("Qual é o seu nome?")
print("")

print(f"Seja bem-vindo {nome} qual é sua idade?")
idade = int ( input ("Digita sua idade aqui"))

tentativa = 0

while tentativa <= 5:
  print(f"A idade digitada foi {idade} voce quer confirma sua idade?")
  print("1. Sim")
  print("2. Não")

  confirma_idade = int(input(""))

  if(confirma_idade == 1):
   if(idade >= 18):
      break

   else:
      print("desculpe menor de idade não é permitido aqui")
      tentativa += 1
    
  elif(confirma_idade == 2):
   print("corrija sua idade")
   idade = idade = int ( input (""))
   tentativa += 1

  else:
   print("Desculpe, não é permitido menor de idade por aqui, porfavor coloque sua idade denovo")
   tentativa += 1

if tentativa >= 5:
 print("Voce bateu o maximo de tentativa")

else:
  login_feito = 1
  
# Daqui estarão as opções de onde ele pode ir

sair_plataforma = 0
habilitar_marketplace = 0

# Sessão de menu inicial
while(habilitar_marketplace == 0 and login_feito == 1 and sair_plataforma == 0):
 print(f"bem-vindo(a) {nome} ao Grupo Solares Marketplace")
 print("------------------------------------------------------------")
 print("Onde você gostaria de ir?")
 print("1. ir no marketplace")
 print("2. ir na area de calculo")
 print("3. ir na area empresarial")
 print("4. Sair da plataforma")

 opcao_menu_inicial = int(input(""))
 if(opcao_menu_inicial == 1):
   habilitar_marketplace += 1

 elif(opcao_menu_inicial == 2):
   print("Esse seguimenteo ainda não está disponivel, porfavor escolha outra opção")

 elif(opcao_menu_inicial == 3):
   
   print("Esse seguimenteo ainda não está disponivel, porfavor escolha outra opção")
 elif(opcao_menu_inicial == 4):
   
   print("Saindo da plataforma...")
   sair_plataforma += 1

 else:
   print("Opção inválida, por favor escolha uma opção válida")


# Sessão de marketplace menu
while(habilitar_marketplace == 1 and login_feito == 1 and sair_plataforma == 0):

  print("Aqui estão as empresas operando no marketplace")
  print(empresas.empresas())
  print("1. Voltar para o menu inicial?")

  opcao_menu_marketplace = int(input(""))

  if(opcao_menu_marketplace == 1):
    habilitar_marketplace -= 1