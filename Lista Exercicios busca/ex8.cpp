#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  char texto[n];

  for (int i = 0; i < n; i++) {
    cin >> texto[i];
  }

  char buscado;
  cin >> buscado;

  bool achou = false;
  for (int i = 0; i < n; i++) {
    if (texto[i] == buscado) {
      achou = true;
      cout << i << " ";
    }
  }

  if (!achou) {
    cout << "-1" << endl;
  } else {
    cout << endl;
  }

  return 0;
}