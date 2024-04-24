#include <iostream>
using namespace std;

int main() {

	int num_de_iteracoes;
	cin >> num_de_iteracoes;

	int valores[num_de_iteracoes];
	int index_ponteiro;

	for (int i = 0; i < num_de_iteracoes; i++) {
		int novo_valor;
		cin >> novo_valor;

		if (novo_valor == 0)
			index_ponteiro -= 2;
		else
			valores[index_ponteiro] = novo_valor;

		index_ponteiro += 1;
	}

	int soma;
	for (int i = 0; i < index_ponteiro; i++)
		soma += valor;
	cout << soma << endl;

	return 0;
}
