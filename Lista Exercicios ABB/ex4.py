import sys
import random

class Noh:
  def __init__(self, v):
    self.valor = v
    self.esq = None
    self.dir = None

class ArvoreBinaria:
  def __init__(self):
    self.raiz = None
  
  def __del__(self):
    self._destruir(self.raiz)
  
  def _inserir_aux(self, noh, valor):
    if noh is None:
      return Noh(valor)
    if valor < noh.valor:
      noh.esq = self._inserir_aux(noh.esq, valor)
    else:
      noh.dir = self._inserir_aux(noh.dir, valor)
    return noh
  
  def _eh_abb_aux(self, noh, min_val, max_val):
    if noh is None:
      return True
    
    if noh.valor <= min_val or noh.valor >= max_val:
      return False
    
    return (self._eh_abb_aux(noh.esq, min_val, noh.valor) and
            self._eh_abb_aux(noh.dir, noh.valor, max_val))
  
  def _em_ordem(self, noh):
    if noh is not None:
      self._em_ordem(noh.esq)
      print(noh.valor, end=" ")
      self._em_ordem(noh.dir)
  
  def _destruir(self, noh):
    if noh is not None:
      self._destruir(noh.esq)
      self._destruir(noh.dir)
      del noh
  
  def inserir(self, valor):
    self.raiz = self._inserir_aux(self.raiz, valor)
  
  def eh_abb(self):
    return self._eh_abb_aux(self.raiz, -sys.maxsize - 1, sys.maxsize)
  
  def inserir_valores_aleatorios(self, quantidade, min_val=1, max_val=100):
    self.raiz = None
    valores = random.sample(range(min_val, max_val + 1), quantidade)
    for valor in valores:
      self.inserir(valor)
    return valores
  
  def criar_arvore_nao_abb(self, quantidade, min_val=1, max_val=100):
    self.raiz = None
    valores = random.sample(range(min_val, max_val + 1), quantidade)
    
    if quantidade > 0:
      self.raiz = Noh(valores[0])
      
      for i in range(1, quantidade):
        self._inserir_manual(self.raiz, valores[i], random.choice([True, False]))
    
    return valores
  
  def _inserir_manual(self, noh_atual, valor, ir_esquerda):
    novo_noh = Noh(valor)
    
    if ir_esquerda:
      if noh_atual.esq is None:
        noh_atual.esq = novo_noh
      else:
        self._inserir_manual(noh_atual.esq, valor, random.choice([True, False]))
    else:
      if noh_atual.dir is None:
        noh_atual.dir = novo_noh
      else:
        self._inserir_manual(noh_atual.dir, valor, random.choice([True, False]))

def main():
  arv = ArvoreBinaria()
  
  print("Escolha uma opcao:")
  print("1 - Inserir valores manualmente")
  print("2 - Gerar arvore ABB aleatoria")
  print("3 - Gerar arvore NAO-ABB aleatoria")
  opcao = int(input("Digite sua opcao: "))
  
  if opcao == 1:
    valores = list(map(int, input("Digite os valores separados por espaco: ").split()))
    for valor in valores:
      arv.inserir(valor)
    print(f"Valores inseridos: {valores}")
  
  elif opcao == 2:
    quantidade = int(input("Digite a quantidade de valores aleatorios: "))
    valores = arv.inserir_valores_aleatorios(quantidade)
    print(f"Valores gerados (ABB): {sorted(valores)}")
  
  elif opcao == 3:
    quantidade = int(input("Digite a quantidade de valores aleatorios: "))
    valores = arv.criar_arvore_nao_abb(quantidade)
    print(f"Valores gerados (NAO-ABB): {valores}")
  
  else:
    print("Opcao invalida!")
    return
  
  print("Arvore em ordem: ", end="")
  arv._em_ordem(arv.raiz)
  print()
  
  if arv.eh_abb():
    print("É uma Árvore ABB")
  else:
    print("Não é uma Árvore ABB")

if __name__ == "__main__":
  main()