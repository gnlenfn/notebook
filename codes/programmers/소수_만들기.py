from itertools import combinations
def solution(nums):
    answer = 0
    pick_3 = combinations(nums, 3)
    sum_of_picks = list(map(sum, pick_3))
    is_prime = sieve(max(sum_of_picks))
    for case in sum_of_picks:
        if case in is_prime:
            answer += 1
    return answer

def sieve(n):
	is_prime = [True] * (n+1)
	is_prime[0] = False
	is_prime[1] = False

	for candidate in range(2, n+1):
		if not is_prime[candidate]:
			continue
		for multiple in range(candidate*candidate, n+1, candidate):
			is_prime[multiple] = False

	return {idx for idx, value in enumerate(is_prime) if value}

print(solution([1,2,3,4]))