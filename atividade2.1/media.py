#import matplotlib.pyplot as plt




from config import run_config, rm_files
run_config()


soma_rr=0
soma_prio=0
soma_fifo=0
soma_sjf=0
count = 0

"""
Média do Round Robin
"""
with open("escalonador_rr/resultado.txt", "r") as file:
	for readline in file: 
		count+=1
		line_strip = readline.strip()
		soma_rr += float(line_strip)

media_aritmetica_rr = soma_rr/count
count=0

"""
Média do de Prioridades
"""
with open("escalonador_prio/resultado.txt", "r") as file:
	for readline in file: 
		count+=1
		line_strip = readline.strip()
		soma_prio += float(line_strip)

media_aritmetica_prio = soma_prio/count
count=0


"""
Média do FIFO
"""
with open("escalonador_fifo/resultado.txt", "r") as file:
	for readline in file: 
		count+=1	
		line_strip = readline.strip()
		soma_fifo += float(line_strip)

media_aritmetica_fifo = soma_fifo/count
count=0

"""
Média do SJF
"""
with open("escalonador_sjf/resultado.txt", "r") as file:
	for readline in file: 
		count+=1	
		line_strip = readline.strip()
		soma_sjf += float(line_strip)

media_aritmetica_sjf = soma_sjf/count

"""
    Apagando o arquivo de resultado e escalonador
"""
rm_files()


"""
Mostrando a média
"""
print(f"Média Escalonador RR:{media_aritmetica_rr}")
print(f"Média Escalonador PRIO:{media_aritmetica_prio}")
print(f"Média Escalonador FIFO:{media_aritmetica_fifo}")
print(f"Média Escalonador SJF:{media_aritmetica_sjf}")

