import heapq
from typing import List, Tuple, Dict
from dataclasses import dataclass

@dataclass
class Aresta:
    u: int
    v: int
    peso: int
    
    def __lt__(self, other):
        return self.peso < other.peso


class UnionFind:
    
    def __init__(self, n: int):
        self.pai = list(range(n))
        self.rank = [0] * n
    
    def encontrar(self, x: int) -> int:
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]
    
    def unir(self, x: int, y: int) -> bool:
        raiz_x, raiz_y = self.encontrar(x), self.encontrar(y)
        if raiz_x == raiz_y:
            return False
        
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1
        return True


class Grafo:
    
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.lista_adjacencia: Dict[int, List[Tuple[int, int]]] = {
            i: [] for i in range(num_vertices)
        }
        self.arestas: List[Aresta] = []
    
    def adicionar_aresta(self, u: int, v: int, peso: int, direcionado: bool = False):
        self.lista_adjacencia[u].append((v, peso))
        self.arestas.append(Aresta(u, v, peso))
        
        if not direcionado:
            self.lista_adjacencia[v].append((u, peso))
    
    def obter_vizinhos(self, vertice: int) -> List[Tuple[int, int]]:
        return self.lista_adjacencia.get(vertice, [])
    
    def imprimir_grafo(self):
        print("\nLista de Adjacência do Grafo:")
        for vertice in range(self.num_vertices):
            vizinhos = self.obter_vizinhos(vertice)
            print(f"Vértice {vertice}: {vizinhos}")


class SistemaTransporteInteligente:
    
    def __init__(self, num_terminais: int):
        self.num_terminais = num_terminais
        self.grafo = Grafo(num_terminais)
    
    def adicionar_rota(self, terminal1: int, terminal2: int, custo: int):
        self.grafo.adicionar_aresta(terminal1, terminal2, custo, direcionado=False)
    
    def arvore_geradora_minima(self) -> Tuple[List[Aresta], int]:
        arestas_ordenadas = sorted(self.grafo.arestas, key=lambda e: e.peso)
        union_find = UnionFind(self.num_terminais)
        arestas_agm = []
        custo_total = 0
        
        for aresta in arestas_ordenadas:
            if union_find.unir(aresta.u, aresta.v):
                arestas_agm.append(aresta)
                custo_total += aresta.peso
                
                if len(arestas_agm) == self.num_terminais - 1:
                    break
        
        return arestas_agm, custo_total
    
    def dijkstra_menores_caminhos(self, origem: int = 0) -> Tuple[Dict[int, int], Dict[int, List[int]]]:
        distancias = {i: float('inf') for i in range(self.num_terminais)}
        distancias[origem] = 0
        anterior = {i: None for i in range(self.num_terminais)}
        visitados = set()
        
        fila_prioridade = [(0, origem)]
        
        while fila_prioridade:
            dist_atual, atual = heapq.heappop(fila_prioridade)
            
            if atual in visitados:
                continue
            
            visitados.add(atual)
            
            for vizinho, peso in self.grafo.obter_vizinhos(atual):
                if vizinho not in visitados:
                    nova_dist = dist_atual + peso
                    
                    if nova_dist < distancias[vizinho]:
                        distancias[vizinho] = nova_dist
                        anterior[vizinho] = atual
                        heapq.heappush(fila_prioridade, (nova_dist, vizinho))
        
        caminhos = {}
        for terminal in range(self.num_terminais):
            if distancias[terminal] != float('inf'):
                caminho = []
                atual = terminal
                while atual is not None:
                    caminho.append(atual)
                    atual = anterior[atual]
                caminhos[terminal] = caminho[::-1]
            else:
                caminhos[terminal] = []
        
        return distancias, caminhos
    
    def analisar_arestas_criticas(self) -> List[Tuple[Aresta, int, int]]:
        arestas_agm, custo_original = self.arvore_geradora_minima()
        analise_critica = []
        
        for aresta_critica in arestas_agm:
            arestas_temp = [e for e in self.grafo.arestas 
                           if not ((e.u == aresta_critica.u and e.v == aresta_critica.v) or
                                  (e.u == aresta_critica.v and e.v == aresta_critica.u))]
            
            arestas_temp_ordenadas = sorted(arestas_temp, key=lambda e: e.peso)
            union_find = UnionFind(self.num_terminais)
            custo_temp = 0
            contador_arestas_temp = 0
            
            for aresta in arestas_temp_ordenadas:
                if union_find.unir(aresta.u, aresta.v):
                    custo_temp += aresta.peso
                    contador_arestas_temp += 1
                    
                    if contador_arestas_temp == self.num_terminais - 1:
                        break
            
            if contador_arestas_temp < self.num_terminais - 1:
                novo_custo = float('inf')
            else:
                novo_custo = custo_temp
            
            impacto = novo_custo - custo_original if novo_custo != float('inf') else float('inf')
            analise_critica.append((aresta_critica, custo_original, novo_custo))
        
        analise_critica.sort(key=lambda x: x[2] - x[1] if x[2] != float('inf') else float('inf'), reverse=True)
        
        return analise_critica
    
    def imprimir_resultados(self):
        print("\n1. ÁRVORE GERADORA MÍNIMA (AGM)")
        print("-" * 50)
        arestas_agm, custo_total = self.arvore_geradora_minima()
        
        print(f"Rotas selecionadas para rede de custo mínimo:")
        for aresta in arestas_agm:
            print(f"  Terminal {aresta.u} -- Terminal {aresta.v} (Custo: {aresta.peso} milhões)")
        print(f"\nCusto total de construção: {custo_total} milhões de reais")
        
        print("\n2. MENORES CAMINHOS DO TERMINAL CENTRA")
        print("-" * 50)
        distancias, caminhos = self.dijkstra_menores_caminhos(0)
        
        for terminal in range(1, self.num_terminais):
            if distancias[terminal] != float('inf'):
                caminho_str = " -> ".join(map(str, caminhos[terminal]))
                print(f"  Para Terminal {terminal}: Tempo = {distancias[terminal]}, Caminho = {caminho_str}")
            else:
                print(f"  Para Terminal {terminal}: Nenhum caminho disponível")
        
        print("\n3. ARESTAS CRÍTICAS")
        print("-" * 50)
        analise_critica = self.analisar_arestas_criticas()
        
        print("Arestas mais críticas (classificadas por impacto):")
        for i, (aresta, custo_original, novo_custo) in enumerate(analise_critica, 1):
            if novo_custo == float('inf'):
                impacto_str = "INFINITO (Rede fica desconectada)"
            else:
                impacto = novo_custo - custo_original
                impacto_str = f"{impacto} milhões de reais"
            
            print(f"  {i}. Terminal {aresta.u} -- Terminal {aresta.v}: Impacto = {impacto_str}")


def main():
    print("Sistema de Transporte Inteligente")
    print("Digite a configuração da rede:")
    
    num_terminais = int(input("Número de terminais (vértices): "))
    sistema = SistemaTransporteInteligente(num_terminais)
    
    num_rotas = int(input("Número de rotas possíveis (arestas): "))
    
    print(f"\nDigite {num_rotas} rotas (formato: terminal1 terminal2 custo):")
    for i in range(num_rotas):
        terminal1, terminal2, custo = map(int, input(f"Rota {i+1}: ").split())
        sistema.adicionar_rota(terminal1, terminal2, custo)
    
    sistema.grafo.imprimir_grafo()
    
    sistema.imprimir_resultados()


if __name__ == "__main__":
    main()