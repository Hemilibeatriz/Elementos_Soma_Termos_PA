# -*- coding: utf-8 -*-
"""Cópia de PAA-FormuladaPA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u_YMA-X8X2NtZKJ_244QwHV9e3nVzkbG

Passamos o último termo an e queremos a razão r
"""

## seria como perguntar quantos ks acontece entre a1 e an
## último termo da PA -->  an = a1 + (k-1).r
## (an-a1)/r + 1 = k
a1=9
an=17
contador = a1
r=2
while (contador <= an):
       print('C') #esse é o k da PA
       contador   = contador + r

"""Soma nos k termos de uma PA"""

primeiro = 9
razao = 2
quant_elem_pa = 6
soma = 0
ultimo = primeiro + (quant_elem_pa - 1)*razao
ultimo = ultimo + 1

for var in range (primeiro, ultimo, razao):
  print(var)
  soma += var
print("Soma de todos os termos: ",soma )