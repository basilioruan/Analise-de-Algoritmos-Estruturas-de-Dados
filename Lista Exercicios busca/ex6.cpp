#include <iostream>
using namespace std;

int buscaBinariaSubstituindo(int n, int *vetor, int buscado, int substituto) {
  int inicio = 0;
  int countOperacoes = 0;
  int fim = n - 1;
  int meio;

  while (inicio <= fim) {
    countOperacoes++;
    meio = (inicio + fim) / 2;
    if (vetor[meio] == buscado) {
      vetor[meio] = substituto;
      inicio = fim + 1;
    } else if (vetor[meio] > meio) {
      inicio = meio + 1;
    } else {
      fim = meio - 1;
    }
  }

  return countOperacoes;
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

  int substituto;
  cin >> substituto;

  int operacoes = buscaBinariaSubstituindo(n, vetor, buscado, substituto);
  for (int i = 0; i < n; i++) {
    cout << vetor[i] << " ";
  }

  cout << endl << operacoes << endl;

  delete[] vetor;

  return 0;
}