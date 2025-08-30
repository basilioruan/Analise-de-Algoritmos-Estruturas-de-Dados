#include <iostream>
using namespace std;

bool isPalindro(int tamPalindromo, string *palindro) {
  int i = 0;
  int j = tamPalindromo - 1;
  bool isPalindro = true;

  if (tamPalindromo == 1) {
    cout << i << " " << palindro[i] << endl;
    return true;
  }

  while (i < j) {
    if (palindro[i] == palindro[j]) {
      cout << i << " " << palindro[i] << " " << j << " " << palindro[j] << " ";
      i++;
      j--;
    } else {
      cout << endl;
      return false;
    }
  }
  cout << endl;

  return true;
}

int main() {
  int tamPalindromo;

  cin >> tamPalindromo;

  string *palindromo = new string[tamPalindromo];

  for (int i = 0; i < tamPalindromo; i++) {
    cin >> palindromo[i];
  }

  if (isPalindro(tamPalindromo, palindromo)) {
    cout << "sim" << endl;
  } else {
    cout << "nao" << endl;
  }

  return 0;
}