#include <iostream>
using namespace std;

int main() {
  char texto[254], chave[254];

  cin >> texto >> chave;

  int tamTexto, tamChave;

  for (int i = 0; texto[i] != '\0'; i++) {
    tamTexto++;
  }
  for (int i = 0; chave[i] != '\0'; i++) {
    tamChave++;
  }
  char chaveCorrigida[tamChave];
  for (int i = 0; i < tamChave; i++) {
    chaveCorrigida[i] = chave[i];
  }

  int countSubString;
  int count = 0;
  bool achou = false;
  char resultTexto[tamChave];
  while (!achou and count <= (tamTexto - tamChave)) {
    countSubString = 0;
    achou = true;
    for (int j = count; j < (count + tamChave); j++) {
      if (texto[j] != chaveCorrigida[countSubString]) {
        achou = false;
      }
      countSubString++;
    }

    if (!achou) {
      count++;
    }
  }

  if (achou) {
    cout << count << endl;
  } else {
    cout << "-1" << endl;
  }

  return 0;
}