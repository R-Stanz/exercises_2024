class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):

        works = zip(difficulty, profit)
        works = sorted(works, key = lambda x: x[0])

        worker.sort(reverse = True)
        
        if (worker[0] < works[0][0]):
            return 0

        limit_indexes = self.search_limits(works, worker)

        return self.max_profit(works, limit_indexes)


    def search_limits(self, works, workers):

        min_worker = workers[-1]
        max_work = len(works) - 1
        max_difficulty = works[max_work][0]

        if (min_worker >= max_difficulty):
            return [max_work for i in workers]

        del min_worker, max_work, max_difficulty


        head = 0
        tail = len(works) - 1
        limit_indexes = []

        while workers:
            worker = workers.pop()

            if (worker >= works[tail][0]):
                limit_indexes.append(tail)
            elif (worker < works[0][0]):
                pass
            else:
                while True:
                    mid = (head + tail) // 2

                    if ((worker >= works[mid][0]) and (worker < works[mid+1][0])):
                        limit_indexes.append(mid)
                        break

                    if (worker < works[mid][0]):
                        tail = mid
                    elif (worker >= works[mid+1][0]):
                        head = mid

            tail = len(works) - 1

        return limit_indexes[::-1]

    
    def max_profit(self, works, limit_indexes):
        
        max_profit = 0
        profits_max_heap = []
        limit = limit_indexes.pop()

        for i in range(len(works)):
            work = works[i]
            heappush(profits_max_heap, -work[1])
            if (i == limit):

                tmp_limit = limit
                while (limit == tmp_limit):
                    max_profit -= profits_max_heap[0]
                    if limit_indexes:
                        limit = limit_indexes.pop()
                    else:
                        break


        max_profit -= len(limit_indexes) * profits_max_heap[0]
        return max_profit
