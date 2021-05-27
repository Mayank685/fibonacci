# Function for nth Fibonacci number
def Fibonacci(n):

	# print incorrect input
	if n < 0:
		print("Incorrect input")

	#  if n is 0
	# t	elif n == 0:
		return 0

	#  if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
print(Fibonacci(9))
