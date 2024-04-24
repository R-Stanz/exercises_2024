#include <iostream>
#include <vector>
using namespace std;

int main() {

	int num_de_iteracoes;
	cin >> num_de_iteracoes;

	vector<int> valores;
	int soma;

	for (int i = 0; i < num_de_iteracoes; i++) {
		int novo_valor;
		cin >> novo_valor;

		if (novo_valor == 0) {
			soma -= valores.back();
			valores.pop_back();
		}
		else {
			soma += novo_valor;
			valores.push_back(novo_valor);
		}
	}

	cout << soma << endl;

	return 0;
}
