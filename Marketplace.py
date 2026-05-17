import csv
import math # Nota importante - para acessar a lista de empresas, é necessário importar o arquivo empresas.py, onde a lista de empresas está definida. Certifique-se de que o arquivo empresas.py esteja no mesmo diretório do arquivo Marketplace.py para que a importação funcione corretamente.
import cadastro


# Sessão de login
login_feito = 0
user_found = False
# opção_login

print("Bem-vindo ao Grupo Solares Marketplace!")
print("------------------------------------------------------------")
print("Qual é sua forma de login?")
print("1. Faça login de usuario")
print("2. Cadastre-se")

login_validação = int(input(""))

if(login_validação == 1):
    email = input("Email: ")
    senha = input("Senha: ")

    with open("cadastro/usuarios.csv", "r", encoding="utf-8") as file:
        leitor = csv.reader(file, delimiter=';')
        next(leitor)

        for linha in leitor:
             if email == linha[2] and senha == linha[3]:
                user_found = True
                print("Login de usuario bem-sucedido!")
                login_feito += 1
             elif user_found == False:
                print("Email ou senha incorretos, por favor tente novamente.")
elif(login_validação == 2):
      print("Vamoas começar o processo de cadastro!")

      nome = input(f"Qual é o seu nome completo?\n ")
      email = input(f"Qual é o seu email? \n ")
      senha = input("Crie uma senha: \n ")
      CEP =  input(f"Qual é o seu CEP? ")
      numero = input(f"qual é o seu numero de telefone? \n ")

      with open("cadastro/usuarios.csv", "r", encoding="utf-8") as file:
        leitor = csv.reader(file, delimiter=';')
        next(leitor)
        
        email_existe = False
        for linha in leitor:
            if linha and len(linha) > 3:  # Verifica se a linha tem pelo menos 4 elementos
             if email == linha[2]:
              print("Esse email ja foi cadastrado, por favor tente novamente com outro email.")
              email_existe = True
              break
             else:
              try:
               proximo_id = 1
               with open("cadastro/usuarios.csv", "r", encoding="utf-8", newline='') as file:
                   leitor = csv.reader(file, delimiter=';')
                   next(leitor)
                   linhas = list(leitor)
                   if linhas and len(linhas) > 0 and linhas[-1] and len(linhas[-1]) > 0:
                     ultimo_id = int(linhas[-1][0])
                     proximo_id = ultimo_id + 1
              except (FileNotFoundError, IndexError, ValueError):
                proximo_id = 1

              with open("cadastro/usuarios.csv", "a", encoding="utf-8", newline='') as file:
                escritor = csv.writer(file, delimiter=';')
                escritor.writerow([proximo_id, nome, email, senha, CEP, numero])
                print("Cadastro realizado com sucesso!")
                login_validação -= 1

        # for linha in leitor:
                

# Daqui estarão as opções de onde ele pode ir

sair_plataforma = 0
habilitar_marketplace = 0

# Sessão de menu inicial
while(habilitar_marketplace == 0 and login_feito == 1 and sair_plataforma == 0):
 print(f"bem-vindo(a) {linha[1]} ao Grupo Solares Marketplace")
 print("------------------------------------------------------------")
 print("Onde você gostaria de ir?")
 print("1. ir no marketplace")
 print("2. ir na area de calculo")
 print("3. ir na area empresarial")
 print("4. Mostrar perfil")
 print("5. Sair da plataforma")

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
while(habilitar_marketplace != 0 and login_feito == 1 and sair_plataforma == 0):

  print("Aqui estão as empresas operando no marketplace")
  with open("cadastro/empresas.csv", "r") as file:
    leitor = csv.reader(file, delimiter=';')
    for line in leitor:
      for idx, line in enumerate(leitor):
        print(f"\n--- linha {idx} ---")
        print(f"Nome: {line[1]}")
        print(f"Cidade: {line[2]}")
        print(f"Tempo de mercado: {line[2]}")
        print(f"Avaliação: {line[4]}")
        print(f"Descrição: {line[5]}")
        print("----------------------")

  print("1. Voltar para o menu inicial?")
  
  opcao_menu_marketplace = int(input(""))
  if(opcao_menu_marketplace == 1):
     habilitar_marketplace -= 1
     print("------------------------------------------------------------")
     print("Onde você gostaria de ir?")
     print("1. ir no marketplace")
     print("2. ir na area de calculo")
     print("3. ir na area empresarial")
     print("4. Sair da plataforma")

     opcao_menu_inicial = int(input(""))

     opcao_menu_inicial