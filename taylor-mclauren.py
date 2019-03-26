soma=0
def factorial(num):
  prod = 1
  while num>1:
    prod *= num
    num -= 1
  return prod


def taylorMcLauren(x, n):
  serie= (x**n)/factorial(n)
  return serie


inp = float(input("Type x number: "))
for i in range(0, 31):
  soma +=(taylorMcLauren(inp, i))
print(soma)
