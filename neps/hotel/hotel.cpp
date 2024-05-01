#include <iostream>
using namespace std;

int main() {

	int base_valor_da_diaria;
	cin >> base_valor_da_diaria;

	int acrescimo_valor_da_diaria;
	cin >> acrescimo_valor_da_diaria;

	int dia_de_chegada;
	cin >> dia_de_chegada;
	int qtd_de_diarias = 31 + 1 - dia_de_chegada;

	int valor_total = base_valor_da_diaria * qtd_de_diarias;
	if (dia_de_chegada < 15)
		valor_total += acrescimo_valor_da_diaria * (dia_de_chegada - 1) *qtd_de_diarias;
	else
		valor_total += acrescimo_valor_da_diaria * 14 * qtd_de_diarias;

	cout << valor_total << endl;

	return 0;
}	
