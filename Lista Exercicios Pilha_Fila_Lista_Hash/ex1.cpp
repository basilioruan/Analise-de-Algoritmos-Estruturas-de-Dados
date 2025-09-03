#include <iostream>

using namespace std;

class Noh {
  friend class Pilha;

 private:
  int dado;  // poderia ser outro tipo de variável
  Noh* proximo;

 public:
  Noh(int info) {
    dado = info;
    proximo = NULL;
  }
  ~Noh() {
    proximo = NULL;
    delete proximo;
  }
};

// pilha dinamicamente encadeada
class Pilha {
 private:
  Noh* topo;
  int tamanho;

 public:
  Pilha();
  ~Pilha();
  void empilha(int info);
  int desempilha();
  void limpaPilha();
  bool estaVazia();  // verifica se existem elementos na pilha
};

Pilha::Pilha() {
  tamanho = 0;
  topo = NULL;
}

Pilha::~Pilha() { limpaPilha(); }

void Pilha::limpaPilha() {
  while (!estaVazia()) {
    desempilha();
  }
  delete topo;
}

void Pilha::empilha(int info) {
  Noh* temporario = new Noh(info);
  temporario->proximo = topo;
  topo = temporario;
  tamanho++;
}

int Pilha::desempilha() {
  if (!estaVazia()) {
    Noh* aux = topo;
    int dado = aux->dado;
    topo = topo->proximo;
    aux->proximo = NULL;
    delete aux;
    tamanho--;

    return dado;
  }

  return -1;
}

bool Pilha::estaVazia() {
  if (topo == NULL)
    return true;
  else
    return false;
}

int main() {
  string expressao;

  getline(cin, expressao);

  Pilha* pilha = new Pilha();

  int lastParenteses = 0;
  int i = 0;
  bool erro = false;

  while (i < expressao.length() and !erro) {
    if (expressao[i] == '(') {
      pilha->empilha(i);
    } else if (expressao[i] == ')') {
      if (pilha->estaVazia()) {
        cout << i << endl;
        erro = true;
      } else {
        pilha->desempilha();
      }
    }
    i++;
  }

  if (!pilha->estaVazia()) {
    cout << pilha->desempilha() << endl;
    erro = true;
  }

  if (!erro) {
    cout << "correto" << endl;
  }
}
