num=600851475143
minor=2 #menor fator
for i in range(0,num):
    if minor >= num: #o menor fator nao pode ser maior que o maior fator
        break
    elif num % minor == 0: # checar se é divisivel por i
        num = num / minor
    else:
        minor= minor + 1
print ("O maior fator primo é: ", str(num))
