# --------------- Função para calculo da Pascoa ---------------#
def calculaDataPascoa(ano):
	g = ano % 19 + 1
	c = ano // 100 + 1
	x = 3*c // 4 - 12
	z = ( 8*c + 5) // 25 - 5
	e = ( 11*g+20+z-x) % 30
	if e == 25 and g > 11 or e == 24:
		e = e + 1
	l = 44-e
	if l < 21:
		l = l+30
	d = 5*ano // 4 - (x+10)
	n = l+7 - (d+l)%7
	if n > 31:
		diaPascoa = n-31
		mesPascoa = 'abril'
	else:
		diaPascoa = n
		mesPascoa = 'março'
	return diaPascoa, mesPascoa
	
# --------------- Função para teste de ano bissexto ---------------#

def testaAnoBissexto(ano):
	if ano % 4 == 0:
		anoBissexto = True
	else:
		anoBissexto = False
	return anoBissexto
	
# --------------- Função para calculo da Paixão de Cristo ---------------#

def calculaDataPaixaoCristo(diaPascoa, mesPascoa):
	if diaPascoa == 1:
		diaPaixao = 31
		mesPaixao = 'março'
	else:
		diaPaixao = diaPascoa - 1
		mesPaixao = mesPascoa
	return diaPaixao, mesPaixao


# --------------- Função para calculo do Corpus Christi ---------------#
	
def calculaDataCorpusChristi(diaPascoa, mesPascoa):
	if diaPascoa == 1:
		diaCorpus = 31
		mesCorpus = 'maio'
	else:
		diaCorpus = diaPascoa - 1
		
	if mesPascoa == 'março':
		mesCorpus = 'maio'
	else:
		mesCorpus = 'junho'
	return diaCorpus, mesCorpus
	
# --------------- Função para calculo do Carnaval ---------------#
if anoBissexto == True:
	x = 29
else:
	x = 28
if mesPascoa == 'abril' and diaPascoa > 16:
	mesCarnaval = 'março'
	diaCarnaval = 31 - ( 47 - diaPascoa )
elif mesPascoa =='abril' and diaPascoa <= 16:
	mesCarnaval = 'fevereiro'
	diaCarnaval = x - ( 31 - ( 47 - diaPascoa))
else:
	mesCarnaval = 'fevereiro'

		
	
# --------------- Função para teste ---------------#

while True:
	ano = int(input("Qual o ano? "))
	anoBissexto = testaAnoBissexto(ano)
	diaPascoa, mesPascoa = calculaDataPascoa(ano)
	diaCorpus, mesCorpus = calculaDataCorpusChristi(diaPascoa, mesPascoa)
	diaPaixao, mesPaixao = calculaDataPaixaoCristo(diaPascoa, mesPascoa)
	anoBissexto = testaAnoBissexto(ano)
	print( 'Pascoa dia', diaPascoa, 'de', mesPascoa)
	print('Corpus Christi dia', diaCorpus, 'de', mesCorpus)
	print('Paixao de Cristo dia', diaPaixao, 'de', mesPaixao)
		
	resposta = input("Deseja reiniciar? ").strip().lower()
	if resposta not in ('s', 'sim'):
	   print("Programa encerrado")
	   break
