#include <iostream>
#include <vector>

using namespace std;

void print(vector<int> vec);
void sort(vector<int>& vec, int tail, int head = 0);
int partition(vector<int>& vec, int tail, int head);


int main() {

	vector<int> vec{1, 10, 20, 2, 30, 3, 9, 1, 99, 99, 2};

	print(vec);
	sort(vec, vec.size() - 1);
	print(vec);

	return 0;
}


void print(vector<int> vec) {
	for (int i : vec)
		cout << i << " ";
	cout << endl;
}

void sort(vector<int>& vec, int tail, int head){
	if (tail > head) {
		int pivot = partition(vec, tail, head);
		sort(vec, pivot - 1, head);
		sort(vec, tail, pivot + 1);
	}
}

int partition(vector<int>& vec, int tail, int head) {
	int pivot = tail;
	for (int i = tail - 1; i >= head; i--) {
		if (vec.at(i) >= vec.at(pivot)) {
			int tmp = vec.at(i);
			for (int u = i; u < pivot; u++)
				vec.at(u) = vec.at(u+1);
			vec.at(pivot) = tmp;
			pivot -= 1;
		}
	}
	return pivot;
}
