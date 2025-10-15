from collections import deque

class Noh:
  def __init__(self, dado):
    self.valor = dado
    self.esq = None
    self.dir = None
    self.pai = None
  
  def nro_de_folhas(self):
    if self.esq is None and self.dir is None:
      return 1
    
    folhas = 0
    if self.esq is not None:
      folhas += self.esq.nro_de_folhas()
    if self.dir is not None:
      folhas += self.dir.nro_de_folhas()
    
    return folhas


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
  
  def nro_de_folhas(self):
    if self.raiz is None:
      return 0
    return self.raiz.nro_de_folhas()


def main():
  qtde = int(input())
  valores = list(map(int, input().split()))
  arvore = ABB()
  
  for i in range(qtde):
    arvore.inserir(valores[i])
  
  print(arvore.nro_de_folhas())

if __name__ == "__main__":
  main()