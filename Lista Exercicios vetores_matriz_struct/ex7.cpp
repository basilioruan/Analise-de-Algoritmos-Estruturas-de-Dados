#include <iostream>
using namespace std;

struct VilaoAlvo {
  string vilao, alvo;
};

struct PlanoVilaoPrejuizo {
  string plano, vilao;
  int prejuizo;
};

void processaAlvo(VilaoAlvo *vilaoAlvo, int qtdVilaoAlvo,
                  PlanoVilaoPrejuizo *planoVilaoPrejuizo,
                  int qtdPlanoVilaoPrejuizo, string alvo) {
  bool achou = false;
  for (int i = 0; i < qtdVilaoAlvo; i++) {
    if (vilaoAlvo[i].alvo == alvo) {
      string vilao = vilaoAlvo[i].vilao;
      for (int j = 0; j < qtdPlanoVilaoPrejuizo; j++) {
        if (planoVilaoPrejuizo[j].vilao == vilao) {
          cout << planoVilaoPrejuizo[j].plano << " "
               << planoVilaoPrejuizo[j].prejuizo << endl;
          achou = true;
        }
      }
    }
  }

  if (!achou) {
    cout << "-1" << endl;
  }
}

int main() {
  int qtdVilaoAlvo, qtdPlanoVilaoPrejuizo;
  cin >> qtdVilaoAlvo;

  VilaoAlvo *vilaoAlvos = new VilaoAlvo[qtdVilaoAlvo];
  string vilao, alvo;
  for (int i = 0; i < qtdVilaoAlvo; i++) {
    cin >> vilao >> alvo;
    vilaoAlvos[i].vilao = vilao;
    vilaoAlvos[i].alvo = alvo;
  }

  cin >> qtdPlanoVilaoPrejuizo;

  PlanoVilaoPrejuizo *planosViloesPrejuizos =
      new PlanoVilaoPrejuizo[qtdPlanoVilaoPrejuizo];
  string plano;
  int prejuizo;
  for (int i = 0; i < qtdPlanoVilaoPrejuizo; i++) {
    cin >> plano >> vilao >> prejuizo;
    planosViloesPrejuizos[i].plano = plano;
    planosViloesPrejuizos[i].vilao = vilao;
    planosViloesPrejuizos[i].prejuizo = prejuizo;
  }

  cin >> alvo;

  processaAlvo(vilaoAlvos, qtdVilaoAlvo, planosViloesPrejuizos,
               qtdPlanoVilaoPrejuizo, alvo);

  return 0;
}