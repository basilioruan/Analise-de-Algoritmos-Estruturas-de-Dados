#include <iostream>
using namespace std;

int *achaSequencia(int tamListaSequencia, int *listaSequencia, int inicio) {
  int contadorSequencia = 1;
  bool achou = false;
  int inicioSequencia = -1;
  for (int i = inicio; i < tamListaSequencia - 1; i++) {
    if (listaSequencia[i] + 1 == listaSequencia[i + 1]) {
      contadorSequencia++;
      achou = true;
      if (inicioSequencia == -1) {
        inicioSequencia = i;
      }
    } else if (achou == true) {
      int *result = new int[2]{inicioSequencia, contadorSequencia};
      return result;
    }
  }

  return NULL;
}

int *achaSequenciaSegundaLista(int tamSequencia, int inicioSequenciaL1,
                               int *listaSequencia, int tamListaVerificadora,
                               int *listaVerificadora,
                               int &countSequenciaLista2) {
  int *sequencia = new int[tamSequencia];
  int countSequencia = 1;
  int valor = listaSequencia[inicioSequenciaL1];
  int countValor = inicioSequenciaL1;
  sequencia[0] = valor;
  for (int i = 0; i < tamListaVerificadora - 1; i++) {
    if (listaVerificadora[i] == valor and
        listaVerificadora[i + 1] == valor + 1) {
      sequencia[countSequencia] = listaVerificadora[i + 1];
      countSequencia++;
      if (countValor < tamSequencia - 1) {
        countValor++;
      } else {
        break;
      }
      valor = listaSequencia[countValor];
    }
  }

  if (countSequencia > 1) {
    int *sequenciaLista2 = new int[countSequencia];
    for (int i = 0; i < countSequencia; i++) {
      sequenciaLista2[i] = sequencia[i];
    }
    countSequenciaLista2 = countSequencia;
    return sequenciaLista2;
  } else {
    return NULL;
  }
}

void processa(int tamListaSequencia, int *listaSequencia,
              int tamListaVerificadora, int *listaVerificadora) {
  int i = 0;
  bool achouPeloMenosUmaSequencia = false;
  int countSequenciaLista2 = 0;
  while (i < tamListaSequencia - 1) {
    int *result = achaSequencia(tamListaSequencia, listaSequencia, i);
    if (result != NULL) {
      int inicioSequencia = result[0];
      int tamSequencia = result[1];
      int *sequenciaLista2 = achaSequenciaSegundaLista(
          tamSequencia, inicioSequencia, listaSequencia, tamListaVerificadora,
          listaVerificadora, countSequenciaLista2);
      if (sequenciaLista2 != NULL) {
        achouPeloMenosUmaSequencia = true;
        for (int i = 0; i < countSequenciaLista2; i++) {
          cout << sequenciaLista2[i] << " ";
        }
        cout << endl;
      }
      i = i + tamSequencia;
      delete[] sequenciaLista2;
    } else {
      i++;
    }
    delete[] result;
  }
  if (!achouPeloMenosUmaSequencia) {
    cout << "ERRO" << endl;
  }
}

int main() {

  int tamLista1, tamLista2;

  cin >> tamLista1 >> tamLista2;

  int *lista1 = new int[tamLista1];
  int *lista2 = new int[tamLista2];

  for (int i = 0; i < tamLista1; i++) {
    cin >> lista1[i];
  }

  for (int i = 0; i < tamLista2; i++) {
    cin >> lista2[i];
  }

  processa(tamLista1, lista1, tamLista2, lista2);
  delete[] lista1;
  delete[] lista2;

  return 0;
}