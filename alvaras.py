import csv
def leia_alvaras(nome_do_arquivo):
	with open(nome_do_arquivo) as dicionario:
		reader = csv.DictReader(dicionario, delimiter=';')
		alvaras = []
		for row in reader:
			alvaras.append(row)
	return alvaras
	
print(leia_alvaras('2015-05-06_Alvaras-Dicionario_de_Dados.csv'))