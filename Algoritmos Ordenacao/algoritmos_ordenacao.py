import time
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import os

def selection_sort(vetor):
    n = len(vetor)
    
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j

        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

    return vetor

def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        key = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > key:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key

    return vetor

def gerar_vetor_aleatorio(tamanho):
    return [random.randint(1, tamanho * 10) for _ in range(tamanho)]

def gerar_vetor_ordenado(tamanho):
    return list(range(1, tamanho + 1))

def gerar_vetor_reverso(tamanho):
    return list(range(tamanho, 0, -1))

def medir_tempo_execucao(func, vetor):
    inicio = time.perf_counter()
    func(vetor)
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def executar_testes_performance():
    tamanhos = [100, 300, 500, 1000, 1500]
    num_execucoes = 10
    
    algoritmos = {
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort
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
            
            for i in range(num_execucoes):
                vetor_melhor_caso = gerar_vetor_ordenado(tamanho)
                tempos_melhor_caso.append(medir_tempo_execucao(funcao_algoritmo, vetor_melhor_caso))

                vetor_caso_medio = gerar_vetor_aleatorio(tamanho)
                tempos_caso_medio.append(medir_tempo_execucao(funcao_algoritmo, vetor_caso_medio))

                vetor_pior_caso = gerar_vetor_reverso(tamanho)
                tempos_pior_caso.append(medir_tempo_execucao(funcao_algoritmo, vetor_pior_caso))

            resultados_finais.append({
                'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Melhor Caso",
                'tempo_medio': statistics.mean(tempos_melhor_caso), 
                'desvio_padrao': statistics.stdev(tempos_melhor_caso) if num_execucoes > 1 else 0
            })
            resultados_finais.append({
                'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Caso Médio",
                'tempo_medio': statistics.mean(tempos_caso_medio), 
                'desvio_padrao': statistics.stdev(tempos_caso_medio) if num_execucoes > 1 else 0
            })
            resultados_finais.append({
                'algoritmo': nome_algoritmo, 'tamanho': tamanho, 'cenario': "Pior Caso",
                'tempo_medio': statistics.mean(tempos_pior_caso), 
                'desvio_padrao': statistics.stdev(tempos_pior_caso) if num_execucoes > 1 else 0
            })
            
    return resultados_finais

def imprimir_tabelas_separadas(resultados):
    algoritmos_unicos = sorted(list(set(res['algoritmo'] for res in resultados)))
    
    for i, nome_algoritmo in enumerate(algoritmos_unicos):
        print("\n" + "=" * 80)
        print(f"Tabela {i+1}: Análise de Performance do {nome_algoritmo}")
        print("=" * 80)
        
        print("| Tamanho (n) | Cenário       | Tempo Médio (ms) | Desvio Padrão (ms) |")
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
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.tight_layout()
        
        nome_arquivo = f"graficos/ordenacao_comparativo_{cenario.replace(' ', '_').lower()}.png"
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo em: {nome_arquivo}")
        plt.close()

    plt.figure(figsize=(14, 8))
    
    cores = {"Selection Sort": "red", "Insertion Sort": "blue"}
    estilos = {"Melhor Caso": "--", "Caso Médio": "-", "Pior Caso": ":"}

    for algoritmo, cor in cores.items():
        for cenario, estilo in estilos.items():
            df_plot = df[(df['algoritmo'] == algoritmo) & (df['cenario'] == cenario)]
            if not df_plot.empty:
                plt.plot(df_plot['tamanho'], df_plot['tempo_medio'], marker='o', 
                         linestyle=estilo, color=cor, label=f'{algoritmo} - {cenario}')

    plt.title('Performance Geral dos Algoritmos de Ordenação', fontsize=16)
    plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (ms) - Escala Logarítmica', fontsize=12)
    plt.xscale('log')
    plt.yscale('log')
    plt.xticks(df['tamanho'].unique(), labels=[str(t) for t in df['tamanho'].unique()], rotation=45)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.grid(True, which="both", ls="--")
    plt.tight_layout(rect=[0, 0, 0.75, 1])

    nome_arquivo_geral = "graficos/ordenacao_comparativo_geral_log.png"
    plt.savefig(nome_arquivo_geral)
    print(f"Gráfico salvo em: {nome_arquivo_geral}")
    plt.close()

def main():
    resultados = executar_testes_performance()
    imprimir_tabelas_separadas(resultados)
    gerar_graficos(resultados)

if __name__ == "__main__":
    main()