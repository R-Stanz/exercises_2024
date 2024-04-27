#include <iostream>
#include <unordered_set>
using namespace std;

int main() {

	string sequencia_de_cartas;
	cin >> sequencia_de_cartas;


	unordered_set<int> cartas_de_copas;
	int quantidade_de_cartas_de_copas = 13;

	unordered_set<int> cartas_de_espadas;
	int quantidade_de_cartas_de_espadas = 13;

	unordered_set<int> cartas_de_ouros;
	int quantidade_de_cartas_de_ouros = 13;

	unordered_set<int> cartas_de_paus;
	int quantidade_de_cartas_de_paus = 13;


	for (int i = 0; i < sequencia_de_cartas.length();) {
		
		int digito_dezena = (int) sequencia_de_cartas[i];
		i += 1;
		int digito_unidade = (int) sequencia_de_cartas[i];
		i += 1;

		int numero_da_carta = digito_dezena*10 + digito_unidade;


		char naipe = sequencia_de_cartas[i];
		i += 1;

		if ((naipe == 'C') && (quantidade_de_cartas_de_copas >= 0)) {
			//if (cartas_de_copas.contains(numero_da_carta))
			if (cartas_de_copas.find(numero_da_carta) != cartas_de_copas.end())
				quantidade_de_cartas_de_copas = -1;
			else {
				cartas_de_copas.insert(numero_da_carta);
				quantidade_de_cartas_de_copas -= 1;
			}
		}

		else if ((naipe == 'E') && (quantidade_de_cartas_de_espadas >= 0)) {
			//if (cartas_de_espadas.contains(numero_da_carta))
			if (cartas_de_espadas.find(numero_da_carta) != cartas_de_espadas.end()) 
				quantidade_de_cartas_de_espadas = -1;
			else {
				cartas_de_espadas.insert(numero_da_carta);
				quantidade_de_cartas_de_espadas -= 1;
			}
		}

		else if ((naipe == 'U') && (quantidade_de_cartas_de_ouros >= 0)) {
			//if (cartas_de_ouros.contains(numero_da_carta))
			if (cartas_de_ouros.find(numero_da_carta) != cartas_de_ouros.end())
				quantidade_de_cartas_de_ouros = -1;
			else {
				cartas_de_ouros.insert(numero_da_carta);
				quantidade_de_cartas_de_ouros -= 1;
			}
		}

		else if ((naipe == 'P') && (quantidade_de_cartas_de_paus >= 0)) {
			//if (cartas_de_paus.contains(numero_da_carta))
			if (cartas_de_paus.find(numero_da_carta) != cartas_de_paus.end())
				quantidade_de_cartas_de_paus = -1;
			else {
				cartas_de_paus.insert(numero_da_carta);
				quantidade_de_cartas_de_paus -= 1;
			}
		}
	}

	if (quantidade_de_cartas_de_copas >= 0)
		cout << 13 - cartas_de_copas.size() << endl;
	else
		cout << "erro" << endl;

	if (quantidade_de_cartas_de_espadas >= 0)
		cout << 13 - cartas_de_espadas.size() << endl;
	else
		cout << "erro" << endl;

	if (quantidade_de_cartas_de_ouros >= 0)
		cout << 13 - cartas_de_ouros.size() << endl;
	else
		cout << "erro" << endl;

	if (quantidade_de_cartas_de_paus >= 0)
		cout << 13 - cartas_de_paus.size() << endl;
	else
		cout << "erro" << endl;

	return 0;
}
