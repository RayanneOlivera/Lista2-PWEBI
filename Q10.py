List = []
for i in range(5):
    n = int (input("Leia um número:"))
    List.append(n)

for i in List:
    if(i %2 == 0):
        print("O número é par", i)
