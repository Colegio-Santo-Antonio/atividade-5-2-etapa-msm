#Maria Clara, Sarah Saldanha, Maria Eduarda Daros
numero = input(  )
numero=list( numero )
impar=[]
par=[]
impar=numero[-1::-2]
impar=[int( i ) for i in impar]
par=numero[-2::-2]
par=[( int( i ) )*2 for i in par]
for i in range( len( par ) ):
  a=0
  divisao=str( par[i] )
  for w in range( len( divisao ) ):
    a+=int( divisao[w] )
  par[i]=a
total=sum( impar )+sum( par )
if total%10==0:
  print( "Cartão válido" )
else:
  print( "Cartão inválido" )

            

# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
