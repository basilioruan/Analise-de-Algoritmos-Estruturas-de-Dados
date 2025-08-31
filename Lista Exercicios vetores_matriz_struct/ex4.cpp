#include <iostream>
using namespace std;

void reposicionaVetor(int inicio, int *vetor, int tamVetor) {
  for (int i = 7; i > inicio; i--) {
    vetor[i] = vetor[i - 1];
  }
}

int main() {
  int vetor[8];
  int valor;
  int count = 0;

  for (int i = 0; i < 8; i++) {
    cin >> valor;

    if (count == 0) {
      vetor[i] = valor;
    } else {
      int j = 0;
      int valorArray;
      bool inseriu = false;
      while (j < count and !inseriu) {
        valorArray = vetor[j];
        if (valor > valorArray) {
          reposicionaVetor(j, vetor, count);
          vetor[j] = valor;
          inseriu = true;
        }
        j++;
      }
      if (!inseriu) {
        vetor[count] = valor;
      }
    }
    count++;
    for (int j = 0; j < count; j++) {
      cout << vetor[j] << " ";
    }
    cout << endl;
  }
}