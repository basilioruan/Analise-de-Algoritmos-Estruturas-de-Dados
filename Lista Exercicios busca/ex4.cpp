#include <iostream>
using namespace std;

void buscaBinaria(int n, int *vetor, int buscado) {
  int inicio = 0;
  int countOperacoes = 0;
  int fim = n - 1;
  int meio;
  int posicao = -1;

  while (inicio <= fim) {
    countOperacoes++;
    meio = (inicio + fim) / 2;
    if (vetor[meio] == buscado) {
      posicao = meio;
      inicio = fim + 1;
    } else if (vetor[meio] < buscado) {
      inicio = meio + 1;
    } else {
      fim = meio - 1;
    }
  }

  cout << posicao << endl << countOperacoes << endl;
}

int main() {
  int n;
  cin >> n;

  int *vetor = new int[n];

  for (int i = 0; i < n; i++) {
    cin >> vetor[i];
  }

  int buscado;
  cin >> buscado;

  buscaBinaria(n, vetor, buscado);

  delete[] vetor;

  return 0;
}