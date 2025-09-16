#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  char* texto = new char[n];

  for (int i = 0; i < n; i++) {
    cin >> texto[i];
  }

  char buscado;
  cin >> buscado;

  bool achou = false;
  int count = 0;
  while (!achou && count < n) {
    if (texto[count] == buscado) {
      achou = true;
    } else {
      count++;
    }
  }

  if (achou) {
    cout << count << endl;
  } else {
    cout << "-1" << endl;
  }

  delete[] texto;
  return 0;
}