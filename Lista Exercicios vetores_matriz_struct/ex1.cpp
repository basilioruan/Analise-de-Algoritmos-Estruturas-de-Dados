#include <iostream>
using namespace std;

bool verificaDuplicidadeLista(string *lista, int tamanhoLista, string valor) {
  bool achou = false;
  for (int i = 0; i < tamanhoLista; i++) {
    if (lista[i] == valor) {
      achou = true;
      cout << lista[i] << endl;
    }
  }

  return achou;
}

int main() {
  int quantidadeElementosLista1;

  cout << "Quantidade elementos lista 1: ";
  cin >> quantidadeElementosLista1;

  string *lista1 = new string[quantidadeElementosLista1];

  for (int i = 0; i < quantidadeElementosLista1; i++) {
    cin >> lista1[i];
  }

  int quantidadeElementosLista2;
  cout << "Quantidade elementos lista 2: ";
  cin >> quantidadeElementosLista2;

  string *lista2 = new string[quantidadeElementosLista2];
  for (int i = 0; i < quantidadeElementosLista2; i++) {
    cin >> lista2[i];
  }

  bool achou = false;
  for (int i = 0; i < quantidadeElementosLista1; i++) {
    if (verificaDuplicidadeLista(lista2, quantidadeElementosLista2,
                                 lista1[i])) {
      achou = true;
    }
  }

  if (!achou) {
    cout << "NADA" << endl;
  }

  delete[] lista1;
  delete[] lista2;

  return 0;
}