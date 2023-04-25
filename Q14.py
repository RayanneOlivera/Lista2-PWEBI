list = []
for i in range(10):
    n = int(input("Digite um número: "))
    list.append(n)
list_ordenada = sorted(list, reverse=True)
print(list_ordenada)

