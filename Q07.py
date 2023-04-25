num = int(input("Digite um número:"))
fb1, fb2, fb3 = 1,0,0

for i in range (num):
  fb3 = fb1 + fb2
  fb1 = fb2
  fb2 = fb3
  print(fb3, end = ",")




