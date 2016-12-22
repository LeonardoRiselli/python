import math
risp=input("per calcolare il volume di un cubo clicca 1, per calcolare il volume della circonferenza scrivi 2: ")
if risp==1:
  l=input("dimmi il valore del lato")
  v= l*l*l
  print"il volume del cubo e': ",v
else:
  r=input("dimmi il valore del raggio: ")
  v= 4.0/3.0*math.pi*r*r*r
  print"il valore del volume e': ",v
