class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):

        all_investments_options = zip(capital, profits)
        all_investments_options = sorted(all_investments_options, key = lambda x: x[0], reverse = True)


        cum_capital = w
        investment_options = []
        new_investment_count  = k

        while (new_investment_count > 0):
            if (not self.add_investment(cum_capital, investment_options, all_investments_options)):
                
                if (not investment_options):
                    return cum_capital

                cum_capital -= heappop(investment_options)
                new_investment_count -= 1

        return cum_capital



    def add_investment(self, capital, investment_options, all_investments_options):
        if (all_investments_options and (capital >= all_investments_options[-1][0])):
            heappush(investment_options, -all_investments_options.pop()[1])
            return True

        return False
