#include <iostream>
using namespace std;

int buscaBinariaRecursiva(int *vetor, int buscado, int inicio, int fim) {
  int meio = (inicio + fim) / 2;

  cout << vetor[meio] << " ";

  if (vetor[meio] == buscado) {
    return meio;
  } else if (inicio < fim) {
    if (vetor[meio] < buscado) {
      buscaBinariaRecursiva(vetor, buscado, meio + 1, fim);
    } else {
      buscaBinariaRecursiva(vetor, buscado, inicio, meio - 1);
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

  buscaBinariaRecursiva(vetor, buscado, 0, n - 1);

  cout << endl;
  delete[] vetor;

  return 0;
}