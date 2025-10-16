import time
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import os

class No:
  def __init__(self, key, parent=None):
    self.key = key
    self.left = None
    self.right = None
    self.parent = parent

class ArvoreBinariaBusca:
  def __init__(self):
    self.root = None
    self.operacoes_count = 0
  
  def tree_insert(self, key):
    self.operacoes_count += 1
    z = No(key)
    
    x = self.root
    y = None
    
    while x is not None:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    
    z.parent = y
    if y is None:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
  
  def iterative_tree_search(self, key):
    self.operacoes_count += 1
    x = self.root
    
    while x is not None and key != x.key:
      if key < x.key:
        x = x.left
      else:
        x = x.right
    
    return x
  
  def tree_minimum(self, node):
    while node.left is not None:
      node = node.left
    return node
  
  def transplant(self, u, v):
    if u.parent is None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    
    if v is not None:
      v.parent = u.parent
  
  def tree_delete(self, z):
    if z is None:
      return
      
    self.operacoes_count += 1
    
    if z.left is None:
      self.transplant(z, z.right)
    elif z.right is None:
      self.transplant(z, z.left)
    else:
      y = self.tree_minimum(z.right)
      
      if y != z.right:
        self.transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      
      self.transplant(z, y)
      y.left = z.left
      y.left.parent = y
  
  def delete_by_key(self, key):
    node = self.iterative_tree_search(key)
    if node:
      self.tree_delete(node)
      return True
    return False
  
  def inorder_traversal(self):
    result = []
    self._inorder_helper(self.root, result)
    return result
  
  def _inorder_helper(self, node, result):
    if node is not None:
      self._inorder_helper(node.left, result)
      result.append(node.key)
      self._inorder_helper(node.right, result)
  
  def height(self):
    return self._height_helper(self.root)
  
  def _height_helper(self, node):
    if node is None:
      return 0
    return 1 + max(self._height_helper(node.left), self._height_helper(node.right))
  
  def size(self):
    return self._size_helper(self.root)
  
  def _size_helper(self, node):
    if node is None:
      return 0
    return 1 + self._size_helper(node.left) + self._size_helper(node.right)
  
  def reset_operations_count(self):
    self.operacoes_count = 0

def gerar_sequencia_aleatoria(tamanho):
  return random.sample(range(1, tamanho * 10), tamanho)

def gerar_sequencia_ordenada(tamanho):
  return list(range(1, tamanho + 1))

def gerar_sequencia_reversa(tamanho):
  return list(range(tamanho, 0, -1))

def gerar_sequencia_balanceada(tamanho):
  if tamanho <= 1:
    return list(range(1, tamanho + 1))
  
  elementos = list(range(1, tamanho + 1))
  sequencia = []
  
  def adicionar_elementos(inicio, fim):
    if inicio <= fim:
      meio = (inicio + fim) // 2
      sequencia.append(elementos[meio])
      adicionar_elementos(inicio, meio - 1)
      adicionar_elementos(meio + 1, fim)
  
  adicionar_elementos(0, len(elementos) - 1)
  return sequencia

def medir_tempo_operacao_abb(operacao, *args):
  inicio = time.perf_counter()
  resultado = operacao(*args)
  fim = time.perf_counter()
  return (fim - inicio) * 1000, resultado

def executar_teste_insercao(sequencia):
  abb = ArvoreBinariaBusca()
  abb.reset_operations_count()
  
  inicio = time.perf_counter()
  for elemento in sequencia:
    abb.tree_insert(elemento)
  fim = time.perf_counter()
  
  tempo_total = (fim - inicio) * 1000
  altura = abb.height()
  tamanho = abb.size()
  
  return {
    'tempo_total': tempo_total,
    'altura': altura,
    'tamanho': tamanho,
    'operacoes': abb.operacoes_count,
    'abb': abb
  }

def executar_teste_busca(abb, elementos_busca):
  abb.reset_operations_count()
  encontrados = 0
  
  inicio = time.perf_counter()
  for elemento in elementos_busca:
    resultado = abb.iterative_tree_search(elemento)
    if resultado is not None:
      encontrados += 1
  fim = time.perf_counter()
  
  tempo_total = (fim - inicio) * 1000
  
  return {
    'tempo_total': tempo_total,
    'encontrados': encontrados,
    'operacoes': abb.operacoes_count
  }

def executar_teste_remocao(abb, elementos_remover):
  abb.reset_operations_count()
  removidos = 0
  
  inicio = time.perf_counter()
  for elemento in elementos_remover:
    if abb.delete_by_key(elemento):
      removidos += 1
  fim = time.perf_counter()
  
  tempo_total = (fim - inicio) * 1000
  
  return {
    'tempo_total': tempo_total,
    'removidos': removidos,
    'operacoes': abb.operacoes_count,
    'altura_final': abb.height(),
    'tamanho_final': abb.size()
  }

def executar_testes_performance():

  # Tamanho reduzido pois estava estourando a pilha de recursão
  tamanhos = [100, 250, 400, 550, 700, 850]
  num_execucoes = 50
  
  operacoes = ["Inserção", "Busca", "Remoção"]
  cenarios = ["Sequência Balanceada", "Sequência Aleatória", "Sequência Ordenada", "Sequência Reversa"]
  
  resultados_finais = []
  
  print("Executando testes de performance da Árvore Binária de Busca...")
  print("=" * 80)
  
  for tamanho in tamanhos:
    print(f"Tamanho da entrada (n) = {tamanho}")
    
    for cenario in cenarios:
      print(f"  - Cenário: {cenario}")
      
      tempos_insercao = []
      tempos_busca = []
      tempos_remocao = []
      alturas = []
      
      for execucao in range(num_execucoes):
        if cenario == "Sequência Balanceada":
          sequencia = gerar_sequencia_balanceada(tamanho)
        elif cenario == "Sequência Aleatória":
          sequencia = gerar_sequencia_aleatoria(tamanho)
        elif cenario == "Sequência Ordenada":
          sequencia = gerar_sequencia_ordenada(tamanho)
        else:
          sequencia = gerar_sequencia_reversa(tamanho)
        
        resultado_insercao = executar_teste_insercao(sequencia)
        tempos_insercao.append(resultado_insercao['tempo_total'])
        alturas.append(resultado_insercao['altura'])
        
        elementos_busca = random.sample(sequencia, max(1, tamanho // 5))
        resultado_busca = executar_teste_busca(resultado_insercao['abb'], elementos_busca)
        tempos_busca.append(resultado_busca['tempo_total'])
        
        elementos_remover = random.sample(sequencia, max(1, tamanho // 10))
        resultado_remocao = executar_teste_remocao(resultado_insercao['abb'], elementos_remover)
        tempos_remocao.append(resultado_remocao['tempo_total'])
      
      for operacao, tempos in [("Inserção", tempos_insercao), ("Busca", tempos_busca), ("Remoção", tempos_remocao)]:
        resultados_finais.append({
          'operacao': operacao,
          'cenario': cenario,
          'tamanho': tamanho,
          'tempo_medio': statistics.mean(tempos),
          'desvio_padrao': statistics.stdev(tempos) if num_execucoes > 1 else 0
        })
  
  return resultados_finais

def imprimir_tabelas_separadas(resultados):
  operacoes_unicas = sorted(list(set(res['operacao'] for res in resultados)))
  
  for i, operacao in enumerate(operacoes_unicas):
    print("\n" + "=" * 100)
    print(f"Tabela {i+1}: Análise de Performance da ABB - Operação: {operacao}")
    print("=" * 100)
    
    print("| Tamanho (n) | Cenário              | Tempo Médio (ms) | Desvio Padrão (ms) |")
    print("|:-----------:|:--------------------:|:----------------:|:------------------:|")
    
    resultados_operacao = [res for res in resultados if res['operacao'] == operacao]
    
    tamanho_atual = None
    for res in resultados_operacao:
      if tamanho_atual is not None and tamanho_atual != res['tamanho']:
        print("|" + "-"*13 + "|" + "-"*22 + "|" + "-"*18 + "|" + "-"*20 + "|")
      
      print(f"| {res['tamanho']:<11} | {res['cenario']:<20} | "
            f"{res['tempo_medio']:>16.6f} | {res['desvio_padrao']:>18.6f} |")
      tamanho_atual = res['tamanho']

def gerar_graficos(resultados):
  print("\n" + "=" * 80)
  print("Gerando gráficos de performance da ABB...")
  print("=" * 80)
  
  if not os.path.exists('graficos'):
    os.makedirs('graficos')
  
  df = pd.DataFrame(resultados)
  
  operacoes = df['operacao'].unique()
  cenarios = df['cenario'].unique()
  
  cores = {"Sequência Balanceada": "green", "Sequência Aleatória": "blue", 
           "Sequência Ordenada": "red", "Sequência Reversa": "orange"}
  
  for operacao in operacoes:
    plt.figure(figsize=(12, 8))
    
    df_operacao = df[df['operacao'] == operacao]
    
    for cenario in cenarios:
      df_cenario = df_operacao[df_operacao['cenario'] == cenario]
      if not df_cenario.empty:
        plt.plot(df_cenario['tamanho'], df_cenario['tempo_medio'], 
                marker='o', linestyle='-', color=cores[cenario], label=cenario)
    
    plt.title(f'Performance da ABB - Operação: {operacao}', fontsize=16)
    plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (ms)', fontsize=12)
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    
    nome_arquivo = f"graficos/abb_{operacao.lower()}_performance.png"
    plt.savefig(nome_arquivo)
    print(f"Gráfico salvo em: {nome_arquivo}")
    plt.close()
  
  plt.figure(figsize=(16, 10))
  
  estilos = {"Inserção": "-", "Busca": "--", "Remoção": ":"}
  
  for operacao, estilo in estilos.items():
    for cenario, cor in cores.items():
      df_plot = df[(df['operacao'] == operacao) & (df['cenario'] == cenario)]
      if not df_plot.empty:
        plt.plot(df_plot['tamanho'], df_plot['tempo_medio'], 
                marker='o', linestyle=estilo, color=cor, 
                label=f'{operacao} - {cenario}')
  
  plt.title('Performance Geral da Árvore Binária de Busca', fontsize=16)
  plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
  plt.ylabel('Tempo Médio de Execução (ms)', fontsize=12)
  plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
  plt.grid(True, which="both", ls="--")
  plt.tight_layout(rect=[0, 0, 0.75, 1])
  
  nome_arquivo_geral = "graficos/abb_performance_geral.png"
  plt.savefig(nome_arquivo_geral)
  print(f"Gráfico salvo em: {nome_arquivo_geral}")
  plt.close()

def demonstrar_funcionamento():
  print("\n" + "=" * 80)
  print("Demonstração do Funcionamento da Árvore Binária de Busca")
  print("=" * 80)
  
  abb = ArvoreBinariaBusca()
  elementos = [15, 10, 20, 8, 12, 25, 6, 11, 13, 22, 27]
  
  print(f"Inserindo elementos: {elementos}")
  for elemento in elementos:
    abb.tree_insert(elemento)
  
  print(f"Percurso em ordem: {abb.inorder_traversal()}")
  print(f"Altura da árvore: {abb.height()}")
  print(f"Tamanho da árvore: {abb.size()}")
  
  print("\nTestando busca:")
  for busca in [10, 25, 30]:
    resultado = abb.iterative_tree_search(busca)
    print(f"  Buscar {busca}: {'Encontrado' if resultado else 'Não encontrado'}")
  
  print("\nTestando remoção:")
  elementos_remover = [10, 15, 25]
  for elemento in elementos_remover:
    if abb.delete_by_key(elemento):
      print(f"  Removido: {elemento}")
      print(f"  Percurso após remoção: {abb.inorder_traversal()}")
    else:
      print(f"  Elemento {elemento} não encontrado para remoção")

def main():
  print("Análise de Performance - Árvore Binária de Busca (ABB)")
  print("=" * 80)
  
  demonstrar_funcionamento()
  
  resultados = executar_testes_performance()
  imprimir_tabelas_separadas(resultados)
  gerar_graficos(resultados)
  
  print("\n" + "=" * 80)
  print("Análise concluída! Verifique os gráficos na pasta 'graficos/'")
  print("=" * 80)

if __name__ == "__main__":
  main()