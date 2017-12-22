#coding: utf-8
from decorators import memoized


def dynamic_programming(number, capacity, weight_cost):
    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    @memoized
    def bestvalue(i, j):
        if i == 0:
            return 0
        weight, cost = weight_cost[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            # maximizing the cost
            return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + cost)

    j = capacity
    result = [0] * number
    for i in xrange(len(weight_cost), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result[i - 1] = 1
            j -= weight_cost[i - 1][0]
    return bestvalue(len(weight_cost), capacity), result
