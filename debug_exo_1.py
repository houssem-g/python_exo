def count_uppercase(lst):
	return sum(letter.isupper() for letter  in''.join(lst))

a = count_uppercase(["SOLO", "hello", "Tea", "wHat"])
print(a)