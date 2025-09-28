import math

# Utilizando classe para representar o struct do C++
class Cliente:
  def __init__(self, nome, x, y, valor):
    self.nome = nome
    self.x = x
    self.y = y
    self.valor = valor
    self.distancia = 0.0

def calcular_distancia(cliente, x_pizzaria, y_pizzaria):
  return math.sqrt((cliente.x - x_pizzaria) ** 2 + (cliente.y - y_pizzaria) ** 2)

def shellsort(clientes):
  n = len(clientes)
  gap = n // 2 # Gap básico do shellsort definido pelo próprio Donald Shell
  
  while gap > 0:
    for i in range(gap, n):
      temp = clientes[i]
      j = i

      while j >= gap and clientes[j - gap].distancia > temp.distancia:
        clientes[j] = clientes[j - gap]
        j -= gap
      
      clientes[j] = temp
    
    gap //= 2

def main():
  n = int(input()) 
  x_pizzaria = float(input()) 
  y_pizzaria = float(input()) 
  total_clientes = int(input()) 
  
  clientes = []
  
  for i in range(total_clientes):
    nome = input().strip()
    x = float(input())
    y = float(input())
    valor = float(input())
    
    cliente = Cliente(nome, x, y, valor)
    cliente.distancia = calcular_distancia(cliente, x_pizzaria, y_pizzaria)
    clientes.append(cliente)
  
  shellsort(clientes)
  
  soma_valores = 0.0
  for i in range(n):
    soma_valores += clientes[i].valor

  print(f"{soma_valores:.2f}")

if __name__ == "__main__":
  main()