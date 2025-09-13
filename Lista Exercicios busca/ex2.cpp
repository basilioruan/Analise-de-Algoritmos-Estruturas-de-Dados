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
  int count = 0;
  while (!achou and count < n) {
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

  return 0;
}