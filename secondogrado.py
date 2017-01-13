import math 
a=float(input("dimmi il valore di a: "))
b=float(input("dimmi il valore di b: "))
c=float(input("dimmi il valore di c: "))
if a==0 and b==0 and c==0:
  print"0=0"
elif a==0 and b==0:
  print"C non puo' essere uguale a 0"
elif a==0:
  x=-c/b
  print"x=",x
else:  
  delta=b*b-4.0*a*c
  if delta>0:
    radicedelta= math.sqrt(delta)
    x1= b*-1.0 + radicedelta / 2.0*a
    x2= b*-1.0 - radicedelta / 2.0*a
    print "x1 e uguale a: ",x1,"e x2 e uguale a: ",x2
  else:
    print " e' impossibile "
