import os

soma=0
soma_rr=0
soma_prio=0
soma_fifo=0
count = 0

os.system("cd escalonador_prio && ./executar.sh")
os.system("cd escalonador_fifo && ./executar.sh")
os.system("cd escalonador_rr && ./executar.sh")


with open("escalonador_rr/resultado.txt", "r") as file:
	for readline in file: 
		count+=1
		line_strip = readline.strip()
		soma_rr += float(line_strip)
count=0
with open("escalonador_prio/resultado.txt", "r") as file:
	for readline in file: 
		count+=1
		line_strip = readline.strip()
		soma_prio += float(line_strip)
count=0
with open("escalonador_fifo/resultado.txt", "r") as file:
	for readline in file: 
		count+=1	
		line_strip = readline.strip()
		soma_fifo += float(line_strip)

media_aritmetica_rr = soma_rr/count
media_aritmetica_prio = soma_prio/count
media_aritmetica_fifo = soma_fifo/count

print(f"Média Escalonador RR:{media_aritmetica_rr}")
print(f"Média Escalonador Prio:{media_aritmetica_prio}")
print(f"Média Escalonador FIFO:{media_aritmetica_fifo}")#print(f"Média:{soma/count}")

