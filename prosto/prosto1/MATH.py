import math

def combination(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def probablity_all_from_first(n, m, k, p):
    total = n +m
    if k > total:
        return None
    if r > n or r > k:
        return 0
    favorable = combination(n, r) * combination(m, k - r)
    all_outcomes = combination(total, k)
    return favorable / all_outcomes