#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int numb_of_divisions;
	cin >> numb_of_divisions;

	int inner_dimension = numb_of_divisions-2;
	if (inner_dimension <= 0) {
		cout << 0 << endl << 0 << endl << 0 << endl;
	}
	else {
		int unpainted_faces = pow(inner_dimension, 3);
		int one_painted_faces = 6*pow(inner_dimension, 2);
		int two_painted_faces = 12*(inner_dimension);

		cout << unpainted_faces << endl;
		cout << one_painted_faces << endl;
		cout << two_painted_faces << endl;
	}

	int three_painted_faces = 8;
	cout << three_painted_faces << endl;

	return 0;
}
