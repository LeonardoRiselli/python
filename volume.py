import math
risp=input("effettua una schelta 1 - CUBO, 2 - SFERA: ")
if risp==1:
  l=input("dimmi il valore del lato: ")
  v= l*l*l
  print"il volume del cubo e': ",v
else:
  r=input("dimmi il valore del raggio: ")
  v= 4.0/3.0*math.pi*r*r*r
  print"il volume e': ",v
