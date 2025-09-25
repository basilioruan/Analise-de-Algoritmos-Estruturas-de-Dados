import time
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import os

def busca_ordenada_linear(vetor, n, k):
  i = 0
  while (i < n and vetor[i] < k):
    i += 1
  if (i < n and vetor[i] == k):
    return i
  return -1

def busca_binaria(vetor, n, k):
  inicio = 0
  fim = n - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == k:
      return meio
    elif vetor[meio] < k:
      inicio = meio + 1
    else:
      fim = meio - 1
  return -1

def gerar_vetor_ordenado(tamanho):
  return sorted([random.randint(1, tamanho * 10) for _ in range(tamanho)])

def medir_tempo_execucao(func, *args):
  inicio = time.perf_counter()
  func(*args)
  fim = time.perf_counter()
  return (fim - inicio) * 1000

def executar_testes_performance():
  tamanhos = [100, 500, 1000, 5000, 10000, 50000, 100000]
  num_execucoes = 50
  
  algoritmos = {
      "Busca Linear Ordenada": busca_ordenada_linear,
      "Busca Binária": busca_binaria
  }
  
  resultados_finais = []
  
  print("Executando testes de performance comparativos...")
  print("=" * 60)
  
  for nome_algoritmo, funcao_algoritmo in algoritmos.items():
    print(f"Testando Algoritmo: {nome_algoritmo}")
    for tamanho in tamanhos:
      print(f"  - Tamanho da entrada (n) = {tamanho}")
      tempos_melhor_caso = []
      tempos_caso_medio = []
      tempos_pior_caso = []
      
      vetores_teste = [gerar_vetor_ordenado(tamanho) for _ in range(num_execucoes)]

      for i in range(num_execucoes):
        vetor = vetores_teste[i]
        
        if nome_algoritmo == "Busca Linear Ordenada":
          chave_melhor_caso = vetor[0]
          chave_caso_medio = vetor[tamanho // 2]
          chave_pior_caso = (tamanho * 10) + 1
        else:
          chave_melhor_caso = vetor[tamanho // 2]
          chave_caso_medio = vetor[random.randint(0, tamanho - 1)]
          chave_pior_caso = (tamanho * 10) + 1

        tempos_melhor_caso.append(medir_tempo_execucao(funcao_algoritmo, vetor, tamanho, chave_melhor_caso))
        tempos_caso_medio.append(medir_tempo_execucao(funcao_algoritmo, vetor, tamanho, chave_caso_medio))
        tempos_pior_caso.append(medir_tempo_execucao(funcao_algoritmo, vetor, tamanho, chave_pior_caso))

      resultados_finais.append({
        'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Melhor Caso",
        'tempo_medio': statistics.mean(tempos_melhor_caso), 'desvio_padrao': statistics.stdev(tempos_melhor_caso) if num_execucoes > 1 else 0
      })
      resultados_finais.append({
        'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Caso Médio",
        'tempo_medio': statistics.mean(tempos_caso_medio), 'desvio_padrao': statistics.stdev(tempos_caso_medio) if num_execucoes > 1 else 0
      })
      resultados_finais.append({
        'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Pior Caso",
        'tempo_medio': statistics.mean(tempos_pior_caso), 'desvio_padrao': statistics.stdev(tempos_pior_caso) if num_execucoes > 1 else 0
      })
      
  return resultados_finais

def imprimir_tabelas_separadas(resultados):
    algoritmos_unicos = sorted(list(set(res['algoritmo'] for res in resultados)))
    
    for i, nome_algoritmo in enumerate(algoritmos_unicos):
        print("\n" + "=" * 80)
        print(f"Tabela {i+1}: Análise de Performance da {nome_algoritmo}")
        print("=" * 80)
        
        print("| Tamanho (n) | Cenário       | Tempo Médio (ms) | Desvio Pádrao (ms) |")
        print("|:-----------:|:-------------:|:----------------:|:------------------:|")

        resultados_algoritmo = [res for res in resultados if res['algoritmo'] == nome_algoritmo]
        
        tamanho_atual = None
        for res in resultados_algoritmo:
            if tamanho_atual is not None and tamanho_atual != res['tamanho']:
                print("|" + "-"*13 + "|" + "-"*15 + "|" + "-"*18 + "|" + "-"*20 + "|")
            
            print(f"| {res['tamanho']:<11} | {res['cenario']:<13} | "
                  f"{res['tempo_medio']:>16.6f} | {res['desvio_padrao']:>18.6f} |")
            tamanho_atual = res['tamanho']

def gerar_graficos(resultados):
    print("\n" + "=" * 80)
    print("Gerando gráficos de performance...")
    print("=" * 80)
    
    if not os.path.exists('graficos'):
        os.makedirs('graficos')

    df = pd.DataFrame(resultados)
    
    cenarios = df['cenario'].unique()
    for cenario in cenarios:
        plt.figure(figsize=(12, 7))
        
        df_cenario = df[df['cenario'] == cenario]
        
        for algoritmo in df_cenario['algoritmo'].unique():
            df_alg = df_cenario[df_cenario['algoritmo'] == algoritmo]
            plt.plot(df_alg['tamanho'], df_alg['tempo_medio'], marker='o', linestyle='-', label=algoritmo)
            
        plt.title(f'Performance Comparativa: {cenario}', fontsize=16)
        plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
        plt.ylabel('Tempo Médio de Execução (ms)', fontsize=12)
        plt.xscale('log')
        plt.yscale('log')
        plt.xticks(df['tamanho'].unique(), labels=[str(t) for t in df['tamanho'].unique()], rotation=45)
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.tight_layout()
        
        nome_arquivo = f"graficos/comparativo_{cenario.replace(' ', '_').lower()}.png"
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo em: {nome_arquivo}")
        plt.close()

    plt.figure(figsize=(14, 8))
    
    cores = {"Busca Linear Ordenada": "red", "Busca Binária": "blue"}
    estilos = {"Melhor Caso": "--", "Caso Médio": "-", "Pior Caso": ":"}

    for algoritmo, cor in cores.items():
        for cenario, estilo in estilos.items():
            df_plot = df[(df['algoritmo'] == algoritmo) & (df['cenario'] == cenario)]
            if not df_plot.empty:
                plt.plot(df_plot['tamanho'], df_plot['tempo_medio'], marker='o', 
                         linestyle=estilo, color=cor, label=f'{algoritmo} - {cenario}')

    plt.title('Performance Geral dos Algoritmos de Busca', fontsize=16)
    plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (ms) - Escala Logarítmica', fontsize=12)
    plt.xscale('log')
    plt.yscale('log')
    plt.xticks(df['tamanho'].unique(), labels=[str(t) for t in df['tamanho'].unique()], rotation=45)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.grid(True, which="both", ls="--")
    plt.tight_layout(rect=[0, 0, 0.75, 1])

    nome_arquivo_geral = "graficos/comparativo_geral_log.png"
    plt.savefig(nome_arquivo_geral)
    print(f"Gráfico salvo em: {nome_arquivo_geral}")
    plt.close()

def main():
  resultados = executar_testes_performance()
  imprimir_tabelas_separadas(resultados)
  gerar_graficos(resultados)

if __name__ == "__main__":
  main()