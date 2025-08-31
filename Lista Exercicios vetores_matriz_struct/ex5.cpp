#include <iostream>
using namespace std;

int getMedia(int **matriz, int i, int j) {
  int divisaoInteira =
      (matriz[i][j] + matriz[i][j - 1] + matriz[i][j + 1] + matriz[i + 1][j] +
       matriz[i - 1][j] + matriz[i - 1][j - 1] + matriz[i + 1][j - 1] +
       matriz[i - 1][j + 1] + matriz[i + 1][j + 1]) /
      9;
  return divisaoInteira;
}

int main() {
  int qtdLinha;
  int qtdColuna;

  cin >> qtdLinha >> qtdColuna;

  int **matriz = new int *[qtdLinha];
  int **matrizResultante = new int *[qtdLinha];

  int valor;
  int col = 0;
  for (int i = 0; i < qtdLinha; i++) {
    matriz[i] = new int[qtdColuna];
    matrizResultante[i] = new int[qtdColuna];
    for (int j = 0; j < qtdColuna; j++) {
      cin >> valor;
      matriz[i][j] = valor;

      if ((i == 0 or i == qtdLinha - 1) or (j == 0 or j == qtdColuna - 1)) {
        matrizResultante[i][j] = valor;
      }
    }
  }
  cout << endl << endl;

  for (int i = 1; i < qtdLinha - 1; i++) {
    for (int j = 1; j < qtdColuna - 1; j++) {
      matrizResultante[i][j] = getMedia(matriz, i, j);
    }
  }

  for (int i = 0; i < qtdLinha; i++) {
    for (int j = 0; j < qtdColuna; j++) {
      cout << matrizResultante[i][j] << " ";
    }
    cout << endl;
  }

  for (int i = 0; i < qtdLinha; i++) {
    delete[] matriz[i];
    delete[] matrizResultante[i];
  }

  delete[] matriz;
  delete[] matrizResultante;

  return 0;
}