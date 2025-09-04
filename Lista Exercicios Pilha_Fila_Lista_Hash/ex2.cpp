#include <iostream>
#include <string>

using namespace std;

class Noh {
  friend class Fila;

 private:
  string dado;  // poderia ser outro tipo de variável
  Noh* proximo;

 public:
  Noh(string info) {
    dado = info;
    proximo = NULL;
  }
  ~Noh() {
    proximo = NULL;
    delete proximo;
  }
};

// fila dinamicamente encadeada
class Fila {
 private:
  Noh* inicio;
  int tamanho;

 public:
  Fila();
  ~Fila();
  void enfileira(string info);
  string desenfileira();
  void limpaFila();
  bool estaVazia();  // verifica se existem elementos na fila
};

Fila::Fila() {
  tamanho = 0;
  inicio = NULL;
}

Fila::~Fila() { limpaFila(); }

void Fila::limpaFila() {
  while (!estaVazia()) {
    desenfileira();
  }
}

void Fila::enfileira(string info) {
  Noh* noh = new Noh(info);

  if (estaVazia()) {
    inicio = noh;
  } else {
    Noh* aux = inicio;
    while (aux->proximo != NULL) {
      aux = aux->proximo;
    }
    aux->proximo = noh;
  }

  tamanho++;
}

string Fila::desenfileira() {
  string removido;
  Noh* temporario;
  removido = inicio->dado;
  temporario = inicio;
  inicio = inicio->proximo;
  delete temporario;
  tamanho--;
  if (estaVazia()) inicio = NULL;

  return removido;
}

bool Fila::estaVazia() {
  if (tamanho == 0)
    return true;
  else
    return false;
}

int main() {
  string instrucao;
  getline(cin, instrucao);

  int countPrioritario = 3;

  Fila* filaPrioridade = new Fila();
  Fila* filaNormal = new Fila();

  while (instrucao != "fim") {
    int pos = instrucao.find(' ');

    if (pos > 0) {
      string tipoFila = instrucao.substr(0, pos);
      string nome = instrucao.substr(pos + 1);

      if (tipoFila == "prioridade") {
        filaPrioridade->enfileira(nome);
      } else {
        filaNormal->enfileira(nome);
      }

    } else {
      if (filaNormal->estaVazia() and filaPrioridade->estaVazia()) {
        cout << "AGUARDE" << endl;
      } else if ((countPrioritario > 0 or filaNormal->estaVazia()) and
                 !filaPrioridade->estaVazia()) {
        cout << filaPrioridade->desenfileira() << endl;
        countPrioritario--;
      } else if ((countPrioritario == 0 or filaPrioridade->estaVazia()) and
                 !filaNormal->estaVazia()) {
        cout << filaNormal->desenfileira() << endl;
        countPrioritario = 3;
      }
    }

    getline(cin, instrucao);
  }

  delete filaNormal;
  delete filaPrioridade;

  return 0;
}
