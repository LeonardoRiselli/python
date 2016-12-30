a=input("dimmi il valore di A: ")
b=input("dimmi il valore di B: ")
b=b*(-1)
a=a*(-1)
if b<0:
  if a%b==0:
    x=a/b
    print"il risultato e': X=",x
  else:
    print"il risutato e': X=",b,"/",a
else:
  if a%b==0:
    x=a/b
    print"il risultato e': X=",x
  else:
    print"il risutato e': X=",b,"/",a
