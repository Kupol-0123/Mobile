print('                    Таблица умнажение')
print()
j=30
h= j*4
s = '     │'
for i in range(1,j+1):
	s = s + ('   '+str(i))[-4:]
print(s)
print('—————'+'┼'+'̶—'*h)
for i in range(1,j+1):
	s = ('   '+ str(i))[-4:] +' │'
	for g in range(1,j+1):
		s = s + ('   ' + str(i*g))[-4:]
	print(s)
