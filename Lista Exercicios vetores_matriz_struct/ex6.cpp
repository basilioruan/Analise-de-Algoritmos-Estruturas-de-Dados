#include <iostream>
using namespace std;

struct SabreLuz {
  string cristal, cor;
};

struct Jedi {
  string nome, posicao;
  SabreLuz sabreLuz;
};

bool insereCorVetor(string *cores, string cor, int countCores) {
  for (int i = 0; i < countCores; i++) {
    if (cor == cores[i]) {
      return false;
    }
  }
  cores[countCores] = cor;
  return true;
}

int contabilizaCorPorHierarquia(Jedi *jedis, string hierarquia, string cor,
                                int qtdCavaleiros) {
  int count = 0;
  for (int i = 0; i < qtdCavaleiros; i++) {
    if (jedis[i].posicao == hierarquia and jedis[i].sabreLuz.cor == cor) {
      count++;
    }
  }

  return count;
}

int main() {
  int qtdCavaleiros;

  cin >> qtdCavaleiros;

  Jedi *jedis = new Jedi[qtdCavaleiros];
  string *cores = new string[qtdCavaleiros];
  int countCores = 0;

  string nome, posicao, cristal, cor;
  for (int i = 0; i < qtdCavaleiros; i++) {
    cin >> nome >> posicao >> cristal >> cor;
    jedis[i].nome = nome;
    jedis[i].posicao = posicao;
    jedis[i].sabreLuz.cristal = cristal;
    jedis[i].sabreLuz.cor = cor;
    if (insereCorVetor(cores, cor, countCores)) {
      countCores++;
    }
  }

  string hierarquia;
  cin >> hierarquia;
  cout << endl << endl;

  for (int i = 0; i < countCores; i++) {
    cout << cores[i] << " "
         << contabilizaCorPorHierarquia(jedis, hierarquia, cores[i],
                                        qtdCavaleiros)
         << endl;
  }

  delete[] jedis;
  delete[] cores;

  return 0;
}