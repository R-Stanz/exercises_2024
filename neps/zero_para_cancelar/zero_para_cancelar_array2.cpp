#include <iostream>
using namespace std;

int main() {

	int num_de_iteracoes;
	cin >> num_de_iteracoes;

	int valores[num_de_iteracoes];
	int index_ponteiro;
	int soma;

	for (int i = 0; i < num_de_iteracoes; i++) {
		int novo_valor;
		cin >> novo_valor;

		if (novo_valor == 0) {
			soma -= valores[index_ponteiro - 1];
			index_ponteiro -= 2;
		}
		else {
			soma += novo_valor;
			valores[index_ponteiro] = novo_valor;
		}

		index_ponteiro += 1;
	}

	cout << soma << endl;

	return 0;
}
