from collections import deque

class Noh:
  def __init__(self, dado):
    self.valor = dado
    self.esq = None
    self.dir = None
    self.contador = 1

class ABB:
  def __init__(self):
    self.raiz = None
  
  def __del__(self):
    self._destruir_recursivo(self.raiz)
  
  def _destruir_recursivo(self, noh):
    if noh is not None:
      self._destruir_recursivo(noh.esq)
      self._destruir_recursivo(noh.dir)
  
  def inserir(self, dado):
    if self.raiz is None:
      self.raiz = Noh(dado)
    else:
      self._inserir_recursivo(self.raiz, dado)
  
  def _inserir_recursivo(self, noh_atual, dado):
    if dado < noh_atual.valor:
      if noh_atual.esq is None:
        novo_noh = Noh(dado)
        noh_atual.esq = novo_noh
        novo_noh.pai = noh_atual
      else:
        self._inserir_recursivo(noh_atual.esq, dado)
    elif dado > noh_atual.valor:
      if noh_atual.dir is None:
        novo_noh = Noh(dado)
        noh_atual.dir = novo_noh
        novo_noh.pai = noh_atual
      else:
        self._inserir_recursivo(noh_atual.dir, dado)
    else:
      noh_atual.contador += 1
  
  def remove(self, chave):
    self.raiz = self._remove_aux(self.raiz, chave)
  
  def _remove_aux(self, noh, chave):
    if noh is None:
      raise RuntimeError("Erro na remoção: chave não encontrada!")

    nova_raiz_sub_arvore = noh
    
    if chave < noh.valor:
      noh.esq = self._remove_aux(noh.esq, chave)
    elif chave > noh.valor:
      noh.dir = self._remove_aux(noh.dir, chave)
    else:
      if (noh.contador > 1):
        noh.contador -= 1
        return nova_raiz_sub_arvore

      if noh.esq is None:
        nova_raiz_sub_arvore = noh.dir
      elif noh.dir is None:
        nova_raiz_sub_arvore = noh.esq
      else:
        nova_raiz_sub_arvore = self._encontra_menor(noh.dir)
        nova_raiz_sub_arvore.dir = self._remove_menor(noh.dir)
        nova_raiz_sub_arvore.esq = noh.esq
      
      del noh
    
    return nova_raiz_sub_arvore
  
  def imprimir_pre_ordem(self):
    self._imprimir_pre_ordem_recursivo(self.raiz, 0)
    print()
  
  def _imprimir_pre_ordem_recursivo(self, noh, nivel):
    if noh is not None:
      print(f"{noh.valor}({noh.contador})/{nivel}", end=" ")
      self._imprimir_pre_ordem_recursivo(noh.esq, nivel + 1)
      self._imprimir_pre_ordem_recursivo(noh.dir, nivel + 1)
    
def main():

  arvore = ABB()
  for i in range(2):
    valores_inserir_10 = list(map(int, input().split()))
    
    for i in range(10):
      arvore.inserir(valores_inserir_10[i])
    
    arvore.imprimir_pre_ordem()
    
    valores_remover_5 = list(map(int, input().split()))

    for i in range(5):
      arvore.remove(valores_remover_5[i])
    arvore.imprimir_pre_ordem()

if __name__ == "__main__":
  main()