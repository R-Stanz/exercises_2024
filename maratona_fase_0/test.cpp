#include <iostream>
#include <map>
#include <unordered_set>

using namespace std;

int main() {
	unordered_set<int> x{2,3,4};
	unordered_set<int> y{1,-2};
	x = x.union(y);
	for (int i : x)
		cout << i << " ";
	cout << endl;

	return 0;
}
