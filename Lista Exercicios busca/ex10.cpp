#include <iostream>
using namespace std;

struct Aluno {
  int matricula;
  string nome;
};

void buscaBinaria(int n, Aluno *vetor, int buscado) {
  int inicio = 0;
  int fim = n - 1;
  int meio;

  while (inicio <= fim) {
    meio = (inicio + fim) / 2;
    cout << vetor[meio].matricula << endl;
    if (vetor[meio].matricula == buscado) {
      cout << vetor[meio].nome << endl;
      inicio = fim + 1;
    } else if (vetor[meio].matricula < buscado) {
      inicio = meio + 1;
    } else {
      fim = meio - 1;
    }
  }
}

int main() {
  int n;
  cin >> n;

  Aluno *alunos = new Aluno[n];

  int matricula, matriculaBuscada;
  string nome;

  for (int i = 0; i < n; i++) {
    cin >> matricula >> nome;
    alunos[i].matricula = matricula;
    alunos[i].nome = nome;
  }

  cin >> matriculaBuscada;
  buscaBinaria(n, alunos, matriculaBuscada);

  return 0;
}
