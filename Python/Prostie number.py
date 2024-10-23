import math

a = int(input("Введите число: "))
c = 1
hol = 2

digit_len = len(str(abs(a)))
for i in range(digit_len - 1):
	c = c * 10
sqrt = math.sqrt(c)

for _ in range(int(sqrt)):
	if a % hol == 0:
		print("Число", a , "Составное")
		break
	else:
		hol += 1