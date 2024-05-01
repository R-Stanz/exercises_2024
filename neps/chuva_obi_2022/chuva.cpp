#include <iostream>
using namespace std;

void popular_hist_de_chuvas (int* hist, int num_de_dias);
int contar_intervalos(int* hist, int num_de_dias, int filtro_chuva_intervalo, int num_de_intervalos = 0, int ini_intervalo = 0);

int main() {

	int num_de_dias;
	cin >> num_de_dias;

	int filtro_chuva_intervalo;
	cin >> filtro_chuva_intervalo;

	int hist_de_chuvas[num_de_dias];
	popular_hist_de_chuvas(hist_de_chuvas, num_de_dias);

	int num_de_intervalos = contar_intervalos(hist_de_chuvas, num_de_dias, filtro_chuva_intervalo);
	cout << num_de_intervalos << endl;

	return 0;
}

void popular_hist_de_chuvas (int* hist, int num_de_dias) {
	for (int i = 0; i < num_de_dias; i++)
		cin >> hist[i];
}

int contar_intervalos(int* hist, int num_de_dias, int filtro_chuva_intervalo, int num_de_intervalos, int ini_intervalo) {
	if (ini_intervalo >= num_de_dias)
		return num_de_intervalos;

	int chuva_acumulada = 0;
	for (int i = ini_intervalo; i < num_de_dias; i++) {
		chuva_acumulada += hist[i];
		
		if (chuva_acumulada > filtro_chuva_intervalo)
			break;
		else if (chuva_acumulada == filtro_chuva_intervalo)
			num_de_intervalos += 1;
		else if ((i+1 == num_de_dias) && (chuva_acumulada < filtro_chuva_intervalo))
			return num_de_intervalos;
	}

	return contar_intervalos(hist, num_de_dias, filtro_chuva_intervalo, num_de_intervalos, ini_intervalo+1);
}
