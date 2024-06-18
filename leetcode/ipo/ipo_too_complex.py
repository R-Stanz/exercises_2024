class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):

        capital_values = sorted(set(capital))
        if (w < capital_values[0]):
            return 0

        capital_profits = {}
        initial_capital = capital_values[0]
        initial_capital_index = 0

        for i in range(len(capital_values) - 1, -1, -1):
        
            if ((i > 0) and (capital_values[i] > w) and (capital_values[i-1] <= w)):
                initial_capital = capital_values[i - 1]
                initial_capital_index = i - 1

            if (capital_values[i] < initial_capital):
                break

            capital_profits[i] = []

        capital_values = capital_values[initial_capital_index:]
        del initial_capital_index


        total_options = len(profits)
        for i in range(total_options):
            if (capital[i] > initial_capital):
                heappush(capital_profits[capital[i]], - profits[i])
            else:
                heappush(capital_profits[initial_capital], - profits[i])
        
        del initial_capital


        total_profit = w
        investments_count = k
        tmp_capital = capital_values[0]

        for u in range(len(capital_values) + 1):

            if ((u > 0) and (u < len(capital_values))):
                capital_profits[tmp_capital] = list(merge(capital_profits[tmp_capital], capital_profits[last_capital]))
            if (u > 1):
                del capital_profits[capital_values[u-2]]

            if (investments_count < 1):
                print("invest")
                break

            if (total_profit < last_capital):
                print("repeat")
                break

            if ((total_profit < tmp_capital) and (total_profit >= last_capital)):
                if (not capital_profits[last_capital]):
                    print("empyt")
                    break

                total_profit -= heappop(capital_profits[last_capital])
                investments_count -= 1

        return total_profit
