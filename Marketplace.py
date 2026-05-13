import math
import empresas # Nota importante - para acessar a lista de empresas, é necessário importar o arquivo empresas.py, onde a lista de empresas está definida. Certifique-se de que o arquivo empresas.py esteja no mesmo diretório do arquivo Marketplace.py para que a importação funcione corretamente.
import cadastro


  login_feito = 0
  
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