#include <iostream>
#include <string>

using namespace std;

const int UMPRIMO = 39;

int funcaoHash(string chave, int limite) {
  int pos = 0;
  for (unsigned i = 0; i < chave.length(); i++)
    pos = (UMPRIMO * pos + chave[i]) % limite;
  return pos;
}

class noh {
  friend class tabelaHash;

 private:
  string chave;
  string valor;
  noh* proximo = NULL;

 public:
  noh(string c, string v) {
    chave = c;
    valor = v;
  }
};

class tabelaHash {
 private:
  // vetor de ponteiros de nós
  noh** elementos;
  int capacidade;

 public:
  // construtor padrão
  tabelaHash(int cap = 100);
  // destrutor
  ~tabelaHash();
  // insere um valor v com chave c
  void insere(string c, string v);
  // recupera um valor associado a uma dada chave
  string recupera(string c);
  // altera o valor associado a uma chave
  void altera(string c, string v);
  // retira um valor associado a uma chave
  void remove(string c);
  // percorrendo a tabela hash (para fins de debug)
  void percorre();
};

// construtor padrão
tabelaHash::tabelaHash(int cap) {
  elementos = new noh*[cap];
  capacidade = cap;
  for (int i = 0; i < cap; i++) elementos[i] = NULL;
}

// destrutor
tabelaHash::~tabelaHash() {
  for (int i = 0; i < capacidade; i++) {
    noh* atual = elementos[i];
    // percorre a lista removendo todos os nós
    while (atual != NULL) {
      noh* aux = atual;
      atual = atual->proximo;
      delete aux;
    }
  }
  delete[] elementos;
}

// Insere um valor v com chave c.
void tabelaHash::insere(string c, string v) {
  int hash = funcaoHash(c, capacidade);

  if (elementos[hash]) {
    noh* novoNoh = new noh(c, v);
    noh* aux = elementos[hash];

    while (aux->proximo) {
      aux = aux->proximo;
    }

    aux->proximo = novoNoh;

  } else {
    noh* novoNoh = new noh(c, v);
    elementos[hash] = novoNoh;
  }
}

// recupera um valor associado a uma dada chave
string tabelaHash::recupera(string c) {
  int h = funcaoHash(c, capacidade);
  if ((elementos[h] != NULL) and (elementos[h]->chave == c)) {
    return elementos[h]->valor;
  } else {
    noh* atual = elementos[h];
    while ((atual != NULL) and (atual->chave != c)) {
      atual = atual->proximo;
    }
    if ((atual != NULL) and (atual->chave == c)) {
      return atual->valor;
    } else {
      return "NAO ENCONTRADO!";
    }
  }
}

// altera o valor associado a uma chave
void tabelaHash::altera(string c, string v) {
  //  CODIGO A SER DESENVOLVIDO

  // imprime "ERRO NA ALTERACAO!" na saída padrão caso tente alterar
  // elemento não existente na tabela

  int hash = funcaoHash(c, capacidade);
  bool achou = false;

  if (elementos[hash] and elementos[hash]->chave == c) {
    elementos[hash]->valor = v;
    achou = true;
  } else if (elementos[hash]) {
    noh* aux = elementos[hash];
    while (aux and !achou) {
      if (aux->chave == c) {
        aux->valor = v;
        achou = true;
      }
      aux = aux->proximo;
    }
  }

  if (!achou) {
    cout << "ERRO NA ALTERACAO!" << endl;
  }
}

// retira um valor associado a uma chave
void tabelaHash::remove(string c) {
  //  CODIGO A SER DESENVOLVIDO

  // imprime "ERRO NA REMOCAO!" na saída padrão caso tente remover
  // elemento não existente na tabela
  int hash = funcaoHash(c, capacidade);
  bool achou = false;
  noh* nohRemocao;

  if (elementos[hash] and elementos[hash]->chave == c) {
    nohRemocao = elementos[hash];
    if (nohRemocao->proximo) {
      elementos[hash] = nohRemocao->proximo;
    } else {
      elementos[hash] = NULL;
    }
    achou = true;
  } else if (elementos[hash]) {
    noh* anterior = elementos[hash];
    noh* nohRemocao = elementos[hash]->proximo;
    while (nohRemocao and !achou) {
      if (nohRemocao->chave == c) {
        achou = true;
        anterior->proximo = nohRemocao->proximo;
      } else {
        nohRemocao = nohRemocao->proximo;
        anterior = anterior->proximo;
      }
    }
  }

  if (!achou) {
    cout << "ERRO NA REMOCAO!" << endl;
  } else {
    nohRemocao->proximo = NULL;
    delete nohRemocao;
    achou = true;
  }
}

// percorre a tabela hash, escrevendo as listas de itens (para fins de debug)
void tabelaHash::percorre() {
  noh* atual;
  for (int i = 0; i < capacidade; i++) {
    cout << i << ":";
    atual = elementos[i];
    while (atual != NULL) {
      cout << "[" << atual->chave << "/" << atual->valor << "]->";
      atual = atual->proximo;
    }
    cout << "NULL  ";
  }
}

int main() {
  tabelaHash th(10);
  int qtdade;
  string chave;
  string valor;

  // insercao na tabela
  cin >> qtdade;
  for (int i = 0; i < qtdade; i++) {
    cin >> chave;
    cin >> valor;
    th.insere(chave, valor);
  }

  // altera valores
  cin >> qtdade;
  for (int i = 0; i < qtdade; i++) {
    cin >> chave;
    cin >> valor;
    th.altera(chave, valor);
  }

  // remove valores
  cin >> qtdade;
  for (int i = 0; i < qtdade; i++) {
    cin >> chave;
    th.remove(chave);
  }

  // recupera valores
  cin >> qtdade;
  for (int i = 0; i < qtdade; i++) {
    cin >> chave;
    cout << th.recupera(chave) << endl;
  }

  // percorre a tabela
  cout << endl;
  th.percorre();
  cout << endl;

  return 0;
}
