import math


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
  print(f"bem-vindo(a) {nome} ao Grupo Solares Marketplace")