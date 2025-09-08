#include <iostream>
#include <stdexcept>

typedef int Dado;  // tipo da informação usada em Lista

class Lista;  // declaração avançada da classe lista

// === Declarações das classes
class Noh {
  friend class Lista;
  friend std::ostream& operator<<(std::ostream& saida, const Lista& l);

 public:
  Noh(const Dado& d, Noh* ptProx = NULL);

 private:
  const Dado mDado;
  Noh* mPtProximo;
};

class Lista {
  friend std::ostream& operator<<(std::ostream& saida, const Lista& l);

 public:
  Lista();
  Lista(const Lista& umaLista);
  ~Lista();
  Lista& operator=(const Lista& umaLista);
  void InserirOrdenado(const Dado& dado);
  inline bool Vazia();
  inline unsigned int Tamanho();
  Dado Ultimo();

 private:
  Noh* mPtPrimeiro;
  Noh* mPtUltimo;
  unsigned int mTamanho;
};

// === Implementações das classes
using namespace std;

Noh::Noh(const Dado& d, Noh* ptProx) : mDado(d), mPtProximo(ptProx) {
  // ptProx tem valor padrão: NULL
}

Lista::Lista() : mPtPrimeiro(NULL), mPtUltimo(NULL), mTamanho(0) {}

Lista::Lista(const Lista& umaLista)
    : mPtPrimeiro(NULL), mPtUltimo(NULL), mTamanho(0) {
  // percorre a lista recebida como parâmetro, copiando os dados
  Noh* ptNoh = umaLista.mPtPrimeiro;
  if (ptNoh != NULL) {  // primeiro valor
    mPtPrimeiro = new Noh(ptNoh->mDado);
    mPtUltimo = mPtPrimeiro;
    ptNoh = ptNoh->mPtProximo;
  }
  while (ptNoh != NULL) {  // outros valores
    mPtUltimo = mPtUltimo->mPtProximo = new Noh(ptNoh->mDado);
    ptNoh = ptNoh->mPtProximo;
  }
}

// destrutor da lista
Lista::~Lista() {
  Noh* iterador = mPtPrimeiro;
  while (iterador != NULL) {
    Noh* aux = iterador;
    iterador = iterador->mPtProximo;
    delete aux;
  }
}

void Lista::InserirOrdenado(const Dado& dado) {
  Noh* noh = new Noh(dado);
  if (Vazia()) {
    mPtPrimeiro = noh;
    mPtUltimo = noh;
  } else if (dado <= mPtPrimeiro->mDado) {
    noh->mPtProximo = mPtPrimeiro;
    mPtPrimeiro = noh;
  } else if (dado > mPtUltimo->mDado) {
    mPtUltimo->mPtProximo = noh;
    mPtUltimo = noh;
  } else {
    Noh* aux = mPtPrimeiro;

    while (dado > aux->mPtProximo->mDado) {
      aux = aux->mPtProximo;
    }

    noh->mPtProximo = aux->mPtProximo;
    aux->mPtProximo = noh;
  }
  mTamanho++;
}

ostream& operator<<(ostream& saida, const Lista& l) {
  Noh* iterador = l.mPtPrimeiro;
  while (iterador != NULL) {
    saida << iterador->mDado << " ";
    iterador = iterador->mPtProximo;
  }
  return saida;
}

inline bool Lista::Vazia() { return mPtPrimeiro == NULL; }

inline unsigned int Lista::Tamanho() { return mTamanho; }

Dado Lista::Ultimo() {
  if (mPtUltimo == NULL)
    throw runtime_error("Consulta do ultimo numa lista vazia.");
  return mPtUltimo->mDado;
}

// === Programa que usa as classes
int main() {
  Dado valor;

  cin >> valor;

  Lista* lista = new Lista();

  while (valor > 0) {
    lista->InserirOrdenado(valor);
    cout << *lista << endl;

    cin >> valor;
  }

  cout << lista->Tamanho() << endl << lista->Ultimo() << endl;

  delete lista;

  return 0;
}
