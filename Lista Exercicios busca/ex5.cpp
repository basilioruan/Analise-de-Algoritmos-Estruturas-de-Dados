#include <iostream>
using namespace std;

int buscaBinariaDecrescenteRecursiva(int *vetor, int buscado, int inicio,
                                     int fim) {
  int meio = (inicio + fim) / 2;

  if (vetor[meio] == buscado) {
    return meio;
  } else if (inicio < fim) {
    if (vetor[meio] > buscado) {
      buscaBinariaDecrescenteRecursiva(vetor, buscado, meio + 1, fim);
    } else {
      buscaBinariaDecrescenteRecursiva(vetor, buscado, inicio, meio - 1);
    }
  } else {
    return -1;
  }
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

  int posicao = buscaBinariaDecrescenteRecursiva(vetor, buscado, 0, n - 1);

  cout << posicao << endl;

  delete[] vetor;

  return 0;
}