def factorial(Z):
    fact = 1
    if Z > 0 :
        for i in range (Z, 1, -1):
            fact *= i
        print(fact)
        return fact
    return fact
		
factorial(3)