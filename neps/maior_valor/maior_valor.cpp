#include <iostream>

using namespace std;

int somar_digitos(int num, int soma = 0);

int main() {

	int limite_inferior;
	cin >> limite_inferior;

	int limite_superior;
	cin >> limite_superior;

	int soma;
	cin >> soma;

	for (int i = limite_superior; i >= limite_inferior; i--) {
		int soma_dos_digitos = somar_digitos(i);
		if (soma == soma_dos_digitos) {
			cout << i << endl;
			return 0;
		}
	}
	cout << -1 << endl;

	return 0;
}

int somar_digitos(int num, int soma) {
	if (num != 0)
		return somar_digitos(num / 10, soma + num % 10);
	return soma;
}
