soma=0
count = 0


with open("resultado.txt", "r") as file:
	for readline in file: 
		count+=1
		line_strip = readline.strip()
		soma += float(line_strip)
print(f"Média:{soma/count}")

