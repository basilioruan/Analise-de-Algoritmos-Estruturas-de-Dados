#include <iostream>
using namespace std;

struct Data {
  int dia, mes, ano;
};

struct Animal {
  int id;
  string nome, dono;
  Data data;
};

bool buscaBinaria(int n, Animal *vetor, int buscado) {
  int inicio = 0;
  int fim = n - 1;
  int meio;

  while (inicio <= fim) {
    meio = (inicio + fim) / 2;
    if (vetor[meio].id == buscado) {
      cout << vetor[meio].nome << " " << vetor[meio].data.dia << "/"
           << vetor[meio].data.mes << "/" << vetor[meio].data.ano << endl;
      return true;
    } else if (vetor[meio].id < buscado) {
      inicio = meio + 1;
    } else {
      fim = meio - 1;
    }
  }
  return false;
}

int main() {
  Animal *animais = new Animal[50];

  int id = -1;
  string nome, dono;
  int dia, mes, ano, idBuscado;
  int count = 0;

  while (id != 0) {
    cin >> id;

    if (id != 0) {
      cin >> nome >> dono >> dia >> mes >> ano;
      animais[count].id = id;
      animais[count].nome = nome;
      animais[count].dono = dono;
      animais[count].data.dia = dia;
      animais[count].data.mes = mes;
      animais[count].data.ano = ano;
      count++;
    }
  }

  cin >> idBuscado;
  bool achou = buscaBinaria(count, animais, idBuscado);

  if (!achou) {
    cout << "inexistente" << endl;
  }

  return 0;
}
