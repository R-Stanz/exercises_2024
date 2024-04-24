#include <iostream>
#include <map>
#include <utility>
using namespace std;

int main() {
	int num_de_iteracoes;
	cin >> num_de_iteracoes;

	map<int,int> amigo_tempo;
	char evento_passado;
	int tempo;
	for (int i = 0; i < num_de_iteracoes; i++) {
		char evento_corrente;
		cin >> evento_corrente;

		int numero;
		cin >> numero;

		if ((evento_passado != 'T') && (evento_corrente != 'T'))
			tempo += 1;

		if (evento_corrente == 'T')
			tempo += numero;

		else if (evento_corrente == 'R') {
			//if (amigo_tempo.contains(numero))
			if (amigo_tempo.find(numero) != amigo_tempo.end())
				amigo_tempo[numero] -= tempo;
			else
				amigo_tempo[numero] = -tempo;
		}

		else if (evento_corrente == 'E') {
			amigo_tempo[numero] += tempo;
		}

		evento_passado = evento_corrente;
	}

	for (auto par : amigo_tempo) {
		cout << par.first << " ";
		if (par.second < 0)
			cout << -1 << endl;
		else
			cout << par.second << endl;
	}

	return 0;
}
