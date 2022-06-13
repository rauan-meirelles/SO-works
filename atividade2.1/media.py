import os

"""
Rodando os algoritmos de escalonamentos
"""
os.system("cd escalonador_prio && gcc -o escalonador escalonador.prio.c")
os.system("cd escalonador_fifo && gcc -o escalonador escalonador.fifo.c")
os.system("cd escalonador_rr && gcc -o escalonador escalonador.rr.c")
os.system("cd escalonador_sjf && gcc -o escalonador escalonador.sjf.c")


"""
Pegando a média dos tempos de espera para cada algoritmo
"""
os.system("cd escalonador_prio && ./executar.sh")
os.system("cd escalonador_fifo && ./executar.sh")
os.system("cd escalonador_rr && ./executar.sh")
os.system("cd escalonador_sjf && ./executar.sh")


soma=0
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
os.system("cd escalonador_prio && rm resultado.txt && rm escalonador")
os.system("cd escalonador_fifo && rm resultado.txt && rm escalonador")
os.system("cd escalonador_rr && rm resultado.txt && rm escalonador")
os.system("cd escalonador_sjf && rm resultado.txt && rm escalonador")



"""
Mostrando a média
"""
print(f"Média Escalonador RR:{media_aritmetica_rr}")
print(f"Média Escalonador PRIO:{media_aritmetica_prio}")
print(f"Média Escalonador FIFO:{media_aritmetica_fifo}")
print(f"Média Escalonador SJF:{media_aritmetica_sjf}")

