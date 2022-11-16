def is_prime(num):
    prime = True
    for i in range(2,num):
        if num <= 1 or num % i == 0:
            prime = False
    return prime


for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
	#print(is_prime(i+1))
