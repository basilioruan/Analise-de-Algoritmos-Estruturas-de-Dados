"""
ABB - Árvore Binária de Busca

Conversão para Python do código original de Joukim, Outubro de 2019 - Estrutura de Dados (GCC216)
Características de implementação:
-> tratamento de exceção
-> usa dado na forma chave/valor
-> uso de métodos recursivos
-> sem duplo encadeamento
-> invés de transplanta, usa removeMenor
"""


class Dado:
  """Classe para representar um dado com chave e valor"""
  
  def __init__(self, chave=0, valor=""):
    self.chave = chave
    self.valor = valor
  
  def __lt__(self, other):
    if isinstance(other, Dado):
      return self.chave < other.chave
    return self.chave < other
  
  def __gt__(self, other):
    if isinstance(other, Dado):
      return self.chave > other.chave
    return self.chave > other
  
  def __eq__(self, other):
    if isinstance(other, Dado):
      return self.chave == other.chave
    return self.chave == other
  
  def __str__(self):
    return f"({self.chave},{self.valor})"
  
  def __repr__(self):
    return self.__str__()


ATIVO = True
INATIVO = False

class Noh:
  """Classe para representar um nó da árvore"""
  
  def __init__(self, dado):
    self.elemento = dado
    self.esq = None
    self.dir = None
    self.situacao = ATIVO


class ABB:
  """Árvore Binária de Busca"""
  
  def __init__(self):
    self.raiz = None
  
  def __del__(self):
    """Destrutor da árvore"""
    self._destruir_recursivamente(self.raiz)
  
  def _destruir_recursivamente(self, noh):
    """Destrutor recursivo, fazendo percorrimento pós-ordem"""
    if noh is not None:
      self._destruir_recursivamente(noh.esq)
      self._destruir_recursivamente(noh.dir)
      del noh
  
  def insere(self, dado):
    """Inserção de um dado na árvore"""
    self.raiz = self._insere_aux(self.raiz, dado)
  
  def _insere_aux(self, noh, dado):
    """Inserção recursiva, devolve nó para atribuição de pai ou raiz"""
    # se chegou em uma folha nula, insere aqui
    if noh is None:
      novo = Noh(dado)
      return novo
    
    # se não é uma folha nula, checa se insere à esquerda ou direita
    if dado < noh.elemento:
      noh.esq = self._insere_aux(noh.esq, dado)
    elif noh.elemento < dado:
      noh.dir = self._insere_aux(noh.dir, dado)
    else:  # não temos elementos repetidos, exercício pede pra atualizar o valor
      noh.elemento.valor = dado
    
    return noh
  
  def _encontra_menor(self, raiz_sub):
    """Nó mínimo (sucessor) de subárvore com raiz em raiz_sub (folha mais à esquerda)"""
    while raiz_sub.esq is not None:
      raiz_sub = raiz_sub.esq
    return raiz_sub
  
  def _remove_menor(self, raiz_sub):
    """Procedimento auxiliar para remover o sucessor substituindo-o pelo seu filho à direita"""
    if raiz_sub.esq is None:  # achou o sucessor
      return raiz_sub.dir
    else:  # não achou ainda, desce mais na subárvore
      raiz_sub.esq = self._remove_menor(raiz_sub.esq)
      return raiz_sub
  
  def remove(self, chave):
    """Remoção recursiva"""
    self.raiz = self._remove_aux(self.raiz, chave)
  
  def _remove_aux(self, noh, chave):
    """Função auxiliar para remoção recursiva"""
    # se chegamos a um nó nulo, então valor não está na árvore
    if noh is None:
      raise RuntimeError("Erro na remoção: chave não encontrada!")
    
    # armazena a nova raiz da subárvore, após remoção
    # caso a remoção não seja no nó atual, ele será retornado
    nova_raiz_sub_arvore = noh
    
    # valor é menor que nó atual, então vai para subárvore esquerda
    if chave < noh.elemento:
      noh.esq = self._remove_aux(noh.esq, chave)
    # valor é maior que nó atual, então vai para subárvore direita
    elif chave > noh.elemento:
      noh.dir = self._remove_aux(noh.dir, chave)
    # valor é igual ao armazenado no nó atual, que deve ser apagado
    else:  # chave == noh.elemento.chave
      if (noh.situacao == ATIVO):
        noh.situacao = INATIVO
        return nova_raiz_sub_arvore

      # nó não tem filhos à esquerda
      if noh.esq is None:
        # troca noh pelo filho à direita
        nova_raiz_sub_arvore = noh.dir
      # nó não tem filhos à direita
      elif noh.dir is None:
        # troca noh pelo filho à esquerda
        nova_raiz_sub_arvore = noh.esq
      # nó tem dois filhos... substituímos pelo sucessor
      else:
        # troca noh pelo sucessor
        nova_raiz_sub_arvore = self._encontra_menor(noh.dir)
        # onde antes estava o sucessor fica agora seu filho à direita
        nova_raiz_sub_arvore.dir = self._remove_menor(noh.dir)
        # filho à esquerda de noh torna-se filho à esquerda de sucessor
        nova_raiz_sub_arvore.esq = noh.esq
      
      # ponteiros ajustados, apagamos o nó
      del noh
    
    # retorna nova raiz da subárvore para ajustes nos níveis acima
    return nova_raiz_sub_arvore
  
  def _percorre_em_ordem_aux(self, atual, nivel):
    """Utiliza o nó atual e seu nível na árvore (para facilitar visualização)"""
    if atual is not None:
      self._percorre_em_ordem_aux(atual.esq, nivel + 1)
      print(f"{atual.elemento}/{nivel}", end=" ")
      self._percorre_em_ordem_aux(atual.dir, nivel + 1)
  
  def imprime(self):
    """Imprime a árvore em ordem"""
    self._percorre_em_ordem_aux(self.raiz, 0)
    print()
  
  def _percorre_ativos_aux(self, atual, nivel):
    """Percorre apenas nós ativos"""
    if atual is not None:
      self._percorre_ativos_aux(atual.esq, nivel + 1)
      if atual.situacao == ATIVO:
        print(f"{atual.elemento}/{nivel}", end=" ")
      self._percorre_ativos_aux(atual.dir, nivel + 1)
  
  def imprime_ativos(self):
    """Imprime apenas elementos ativos (em ordem)"""
    self._percorre_ativos_aux(self.raiz, 0)
    print()
  
  def _percorre_inativos_aux(self, atual, nivel):
    """Percorre apenas nós inativos"""
    if atual is not None:
      self._percorre_inativos_aux(atual.esq, nivel + 1)
      if atual.situacao == INATIVO:
        print(f"{atual.elemento}/{nivel}", end=" ")
      self._percorre_inativos_aux(atual.dir, nivel + 1)
  
  def imprime_inativos(self):
    """Imprime apenas elementos inativos (em ordem)"""
    self._percorre_inativos_aux(self.raiz, 0)
    print()


def main():
  """Função principal para testar a árvore"""
  arvore = ABB()
  
  while True:
    try:
      entrada = input().strip().split()
      
      operacao = entrada[0].lower()
      
      match operacao:
        case 'i':  # Inserir recursivamente
          chave = int(entrada[1])
          valor = entrada[2]
          dado = Dado(chave, valor)
          arvore.insere(dado)
          
        case 'r':  # Remover recursivamente
          chave = int(entrada[1])
          arvore.remove(chave)
          
        case 'p':  # Escrever tudo (em ordem)
          print("$:", end="")
          arvore.imprime()
          
        case 'a':  # Imprime elementos ativos (em ordem)
          print("@:", end="")
          arvore.imprime_ativos()
          
        case 'z':  # Imprime elementos inativos (em ordem)
          print("#:", end="")
          arvore.imprime_inativos()
          
        case 'f':  # Finalizar execução
          break
          
        case _:  # Default - comando inválido
          print("Comando inválido!")
        
    except RuntimeError as e:
      print(f"Erro: {e}")
    except ValueError:
      print("Erro: Chave deve ser um número inteiro!")
    except Exception as e:
      print(f"Erro inesperado: {e}")


if __name__ == "__main__":
  main()