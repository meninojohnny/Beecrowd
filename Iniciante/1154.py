cont = 0
soma = 0
while True:
	n = int(input())
	if n < 0:
		break
	cont += 1
	soma += n
media = soma / cont
print('%.2f' %media)
