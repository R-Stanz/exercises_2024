#include <iostream>
using namespace std;

void ordenar_contas (int* contas);

int main() {

	int valor_disp;
	cin >> valor_disp;

	int contas[3];
	for (int i = 0; i < 3; i++)
		cin >> contas[i];

	ordenar_contas(contas);

	int soma_contas_pagas = 0;
	int num_de_contas_pagas = 0;
	for (int i : contas) {
		if (soma_contas_pagas + i <= valor_disp) {
			soma_contas_pagas += i;
			num_de_contas_pagas += 1;
		}
		else
			break;
	}
	cout << num_de_contas_pagas << endl;

	return 0;
}

void ordenar_contas(int* contas) {
	for (int i = 0; i < 2; i++) {
		for (int u = i+1; u < 3; u++) {
			if (contas[i] > contas[u]) {
				int tmp = contas[i];
				contas[i] = contas[u];
				contas[u] = tmp;
			}
		}
	}
}
