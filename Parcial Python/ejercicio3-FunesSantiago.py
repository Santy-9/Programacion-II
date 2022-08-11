#Funes Santiago
#41489259

def tribonacci(n):
	''' tribonacci : Int -> Int
		Recibe un numero y calcula el tribonacci
		tribonacci(1) = 0
		tribonacci(4) = 2
		tribonacci(7) = 13
		tribonacci(19) = 19513
	'''
	if(n == 0):
		return 0
	elif(n == 1):
		return 0
	elif(n == 2):
		return 1
	else:
		return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
		
def test_tribonacci():
	assert(tribonacci(1)) == 0
	assert(tribonacci(4)) == 2
	assert(tribonacci(7)) == 13
	assert(tribonacci(19)) == 19513


