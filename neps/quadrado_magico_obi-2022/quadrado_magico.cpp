#include <iostream>

using namespace std;

int somar_linha(int mat[], int dim);

int main() {

	int dim;
	cin >> dim;

	int mat[dim][dim];

	int linha_inelegivel;
	int col_inelegivel;

	for (int linha = 0; linha < dim; linha++) {
		for (int col = 0; col < dim; col++) {
			int valor;
			cin >> valor;
			mat[linha][col] = valor;

			if (valor == 0) {
				linha_inelegivel = linha;
				col_inelegivel = col;
			}
		}
	}

	int soma_magica;
	if (linha_inelegivel == 0)
		soma_magica = somar_linha(mat[linha_inelegivel + 1], dim);
	else 
		soma_magica = somar_linha(mat[linha_inelegivel - 1], dim);

	int numero_inelegivel = soma_magica - somar_linha(mat[linha_inelegivel], dim);
	cout << numero_inelegivel << endl;
	cout << linha_inelegivel + 1 << endl;
	cout << col_inelegivel + 1 << endl;

	return 0;
}

int somar_linha(int mat[], int dim) {
	int soma = 0;
	for (int i = 0; i < dim; i++) 
		soma += mat[i];
	return soma;
}
