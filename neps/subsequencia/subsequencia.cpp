#include <iostream>

using namespace std;

int main() {

	int tamanho_da_sequencia;
	cin >> tamanho_da_sequencia;

	int tamanho_da_subsequencia;
	cin >> tamanho_da_subsequencia;

	int sequencia[tamanho_da_sequencia];
	for (int i = 0; i < tamanho_da_sequencia; i++)
		cin >> sequencia[i];

	int subsequencia[tamanho_da_subsequencia];
	for (int i = 0; i < tamanho_da_subsequencia; i++)
		cin >> subsequencia[i];

	for (int i = 0; i < tamanho_da_sequencia; i++) {
		int marcador_sequencia = 0;
		int marcador_subsequencia = 0;
		while (sequencia[i + marcador_sequencia] == subsequencia[marcador_subsequencia]) {
			marcador_sequencia += 1;
			marcador_subsequencia += 1;
			if(marcador_subsequencia == tamanho_da_subsequencia) {
				cout << "S" << endl;
				return 0;
			}
			while ((i + marcador_sequencia < tamanho_da_sequencia) and (sequencia[i + marcador_sequencia] != subsequencia[marcador_subsequencia]))
				marcador_sequencia += 1;
		}
	}

	cout << "N" << endl;

	return 0;
}
