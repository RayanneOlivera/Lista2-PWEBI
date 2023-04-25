list = []
list = input("Digite uma lista de números: ").split() #Digite os números separados por espaço
x = int(input("Qual número você procura? "))
if str(x) in list:
    print(f"O número {x} está na lista!")
else:
    print(f"O número {x} não está na lista!")

