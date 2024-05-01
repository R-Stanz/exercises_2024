#include <iostream>

using namespace std;

bool eh_subsequencia(int* sequencia, int* subsequencia, 
			int tamanho_da_sequencia, int tamanho_da_subsequencia,
			int marcador_sequencia, int marcador_subsequencia = 0);

int ajustar_marcador_sequencia(int proxm_val, int* sequencia, int tamanho_da_sequencia, int marcador_sequencia);

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
		if (sequencia[i] == subsequencia[0]) {
			if (eh_subsequencia(sequencia, subsequencia, tamanho_da_sequencia, tamanho_da_subsequencia, i)) {
				cout << "S" << endl;
				return 0;
			}
		}
	}

	cout << "N" << endl;

	return 0;
}

bool eh_subsequencia(	int* sequencia, int* subsequencia, 
			int tamanho_da_sequencia, int tamanho_da_subsequencia,
			int marcador_sequencia, int marcador_subsequencia) {

	if (marcador_subsequencia == tamanho_da_subsequencia)
		return true;

	if (marcador_subsequencia + 1 != tamanho_da_subsequencia)
		marcador_sequencia = ajustar_marcador_sequencia(subsequencia[marcador_subsequencia + 1], sequencia, tamanho_da_sequencia, marcador_sequencia);

	if (marcador_sequencia == tamanho_da_sequencia)
		return false;

	return eh_subsequencia(sequencia, subsequencia, tamanho_da_sequencia, tamanho_da_subsequencia, marcador_sequencia, marcador_subsequencia + 1);
}

int ajustar_marcador_sequencia(int proxm_val, int* sequencia, int tamanho_da_sequencia, int marcador_sequencia) {
	if (marcador_sequencia == tamanho_da_sequencia)
		return marcador_sequencia;
	else if (sequencia[marcador_sequencia] == proxm_val)
		return marcador_sequencia;

	return ajustar_marcador_sequencia(proxm_val, sequencia, tamanho_da_sequencia, marcador_sequencia + 1);
}
