## Factorial of n
## Again iteration would be better...
## iteration is better for decrease and conquer
def factorial_of(n):
	if n == 0:
		return 1
	else:
		n * factorial_of(n-1)