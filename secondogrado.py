import math 
a=input("dimmi il valore di a: ")
b=input("dimmi il valore di b: ")
c=input("dimmi il valore di c: ")
delta=b*b-4.0*a*c
if delta>0:
  radicedelta= math.sqrt(delta)
  x1= (b*(-1.0)) + radicedelta / (2.0*a)
  x2= (b*(-1.0)) - radicedelta / (2.0*a)
  print "x1 e uguale a: ",x1,"e x2 e uguale a: ",x2
else:
  print " e' impossibile "
