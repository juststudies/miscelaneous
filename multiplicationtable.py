cores = {'limpa':'\033[m',
'azul':'\033[34m','amarelo':'\033[33m'}

print("{}PROGRAMA{} DE {}TABUADA{}!!!".format(cores['azul'],cores['limpa'], cores['amarelo'], cores['limpa']))

while True:
  usr= int(input("Insira o primeiro fator: "))
  lim = int(input("Segundo fator: (em dezenas)  "))
  if lim <= 100:
    for i in range(1,lim+1):
      print(usr, "X", i, "=", usr*i)
    c = str(input("Deseja colocar um novo numero? s/n "))
    if c == 'n' or len(c) == 0:
      print("Ok, até mais {}õ/{}".format(cores['amarelo'],cores['limpa']))
      break
  else:
    print("{}Dá{} não {}parcero{} >:C".format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
    break
