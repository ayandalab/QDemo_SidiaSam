"""
PRACTICE TEST - CODILITY
"""
def duplicates(A):
	return list(dict.fromkeys(A))

def getFullSum(A):
	Maximum = max(A)
	sum = 0
	for i in range(Maximum+1):
		sum = sum + i
	return sum

def sumOfArr(A):
	if sum(A) <= 0:
		return -1
	return sum(A)

def solution(A):
	A = duplicates(A)
	FSum = getFullSum(A)
	Sum = sumOfArr(A)
	return FSum - Sum

	
"""
QUESTION 1
"""
def filter_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    news = s[0:2]
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            news += s[i]
    return news


def solution(S):
	Three_letters = S[0:2]
	for i in range(2, len(S)):
		if S[i] != S[i-1] or S[i] != S[i-2]:
			Three_letters += S[i]
	return Three_letters

if __name__ == '__main__':
    s = input()
    res = solution(s)
    print(res)
	
	
"""
QUESTION 3
"""
def solution(N):
	enable_print = N % 10
	while(N>0):
		if enable_print == 0 and N%10 != 0:
			enable_print = 1
		if enable_print >= 1:
		    print(N%10, end="")
		N = N//10
		

"""
QUESTION 2
"""
def solution(S):
	if len(S) == 2:
		return 1
	workers = 0
	lCount, rCount = 0,0

	for i in S:
		if i == "L": lCount = lCount + 1
		else: rCount = rCount + 1

		if lCount == rCount: workers = workers + 1

	return workers
