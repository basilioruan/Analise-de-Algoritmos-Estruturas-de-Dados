#include <iostream>
using namespace std;

int achaPosicaoL1(int *l1, int n, int buscado) {
  bool achou = false;
  int count = 0;

  while (!achou and count < n) {
    if (l1[count] == buscado) {
      achou = true;
    } else {
      count++;
    }
  }

  return count;
}

int achaPosicaoL2(int *l2, int n, int buscado) {
  bool achou = false;
  int count = n - 1;

  while (!achou and count >= 0) {
    if (l2[count] == buscado) {
      achou = true;
    } else {
      count--;
    }
  }

  return count;
}

int main() {
  int n;
  cin >> n;
  int *l1 = new int[n];
  int *l2 = new int[n];

  for (int i = 0; i < n; i++) {
    cin >> l1[i];
  }

  for (int i = 0; i < n; i++) {
    cin >> l2[i];
  }

  int buscado;
  cin >> buscado;

  int p1 = achaPosicaoL1(l1, n, buscado);
  int p2 = achaPosicaoL2(l2, n, buscado);

  if (p1 > p2) {
    int aux = p1;
    p1 = p2;
    p2 = aux;
  }

  for (int i = p1; i <= p2; i++) {
    cout << l1[i] << endl;
  }

  for (int i = p1; i <= p2; i++) {
    cout << l2[i] << endl;
  }

  delete[] l1;
  delete[] l2;

  return 0;
}