#include <iostream>
#include <vector>
using namespace std;

void popular_estoque(vector<vector<int>>& estoque, int tipos, int tamanhos);

int main() {

	int qtd_de_tipos;
	cin >> qtd_de_tipos;

	int qtd_de_tamanhos;
	cin >> qtd_de_tamanhos;

	vector<vector<int>> estoque;
	popular_estoque(estoque, qtd_de_tipos, qtd_de_tamanhos);

	int num_de_pedidos;
	cin >> num_de_pedidos;

	int total_de_vendas = 0;
	for (int i = 0; i < num_de_pedidos; i++) {
		int tipo;
		cin >> tipo;

		int tamanho;
		cin >> tamanho;

		auto& itens_do_pedido = estoque.at(tipo - 1).at(tamanho - 1);
		if (itens_do_pedido != 0) {
			itens_do_pedido -= 1;
			total_de_vendas += 1;
		}
	}
	
	cout << total_de_vendas << endl;
	
	return 0;
}

void popular_estoque(vector<vector<int>>& estoque, int tipos, int tamanhos) {
	for (int i = 0; i < tipos; i++) {
		vector<int> tamanho_nos_tipos;
		for (int u = 0; u < tamanhos; u++) {
			int qtd_do_tamanho;
			cin >> qtd_do_tamanho;
			tamanho_nos_tipos.push_back(qtd_do_tamanho);
		}
		estoque.push_back(tamanho_nos_tipos);
	}
}
