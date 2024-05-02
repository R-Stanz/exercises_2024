#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool eh_valida(unordered_map<int,unordered_set<int>>& caminhos, int* rota, int tamanho_da_rota, int marcador = 0);

int main() {

	int num_de_saloes;
	cin >> num_de_saloes;

	int num_de_caminhos;
	cin >> num_de_caminhos;

	unordered_map<int,unordered_set<int>> caminhos;

	for (int i = 0; i < num_de_caminhos; i++) {
		int salao_a;
		int salao_b;

		cin >> salao_a >> salao_b;

		caminhos[salao_a].insert(salao_b);
		caminhos[salao_b].insert(salao_a);
	}

	int num_de_sugestoes;
	cin >> num_de_sugestoes;
	int rotas_validas = 0;
	for (int i = 0; i < num_de_sugestoes; i++) {
		int tamanho_da_rota;
		cin >> tamanho_da_rota;
		int rota[tamanho_da_rota];

		for (int& salao : rota)
			cin >> salao;

		if(eh_valida(caminhos, rota, tamanho_da_rota))
			rotas_validas += 1;
	}

	cout << rotas_validas << endl;

	return 0;
}


bool eh_valida(unordered_map<int,unordered_set<int>>& caminhos, int* rota, int tamanho_da_rota, int marcador) {
	if (marcador + 1 == tamanho_da_rota)
		return true;

	//if(caminhos.contais(rota[marcador))
	if (caminhos.find(rota[marcador]) != caminhos.end()) {
		unordered_set<int>& caminhos_possiveis = caminhos[rota[marcador]];

		//if (caminhos_possiveis.contains(rota[marcador+1]))
		if (caminhos_possiveis.find(rota[marcador+1]) != caminhos_possiveis.end())
			return eh_valida(caminhos,rota, tamanho_da_rota, marcador + 1);
	}
	return false;
}
