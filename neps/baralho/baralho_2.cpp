#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {

	unordered_map<char, pair<unordered_set<int>, bool>> all_kinds_cards;

	char kinds[]{'C','E','U','P'};
	for (char kind : kinds) 
		all_kinds_cards[kind];

	string sequence;
	cin >> sequence;

	for (int i = 0; i < sequence.length();) {
		int card_numb_first_digit = (int) sequence[i];
		i += 1;

		int card_numb_second_digit = (int) sequence[i];
		i += 1;

		int card_numb = card_numb_first_digit * 10 + card_numb_second_digit;

		char kind = sequence[i];
		i += 1;

		bool &kind_has_error = all_kinds_cards[kind].second;
		if (not kind_has_error) {
			unordered_set<int>& cards = all_kinds_cards[kind].first;

			if (cards.find(card_numb) != cards.end())
				kind_has_error = true;
			else
				cards.insert(card_numb);
		}
	}

	for (auto kind : kinds) {
		bool &has_error = all_kinds_cards[kind].second;
		if (has_error)
			cout << "erro" << endl;
		else {
			auto &cards = all_kinds_cards[kind].first;
			cout << 13 - cards.size() << endl;
		}
	}

	return 0;
}
