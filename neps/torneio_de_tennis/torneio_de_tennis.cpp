#include <iostream>
using namespace std;

int main() {

	int vitorias;

	for (int i = 0; i < 6; i++) {
		char resultado;
		cin >> resultado;

		if (resultado == 'V')
			vitorias += 1;
	}

	if (vitorias == 0)
		cout << "-1" << endl;
	else
		cout << 3 - ((vitorias - 1) / 2) << endl;

	return 0;
}
