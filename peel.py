nth = int(input("Digite o numero: "))
lpeel = [1, nth]
for i in range (2, 10):
  peel = 2*(lpeel[-2]) + lpeel[-1]
  lpeel.append(peel)
  print(lpeel)
