'''
   Progamador....: (C) 2025 Pedro Sousa
   Data..........: 14/02/2025
   Observações...: Tabela de verdade do AND e do OR
'''

print("Tabela de Verdade do AND")
print(f" A  B  |  F = A AND B  ")
print(f" 0  0  |  {False and False}")
print(f" 0  1  |  {False and True}")
print(f" 1  0  |  {True and False}")
print(f" 1  1  |  {True and True}") 

print("\nTabela de Verdade do OR")
print(f" A  B  |  F = A OR B   ")
print(f" 0  0  |  {False or False}")
print(f" 0  1  |  {False or True}")
print(f" 1  0  |  {True or  False}")
print(f" 1  1  |  {True or True}") 
