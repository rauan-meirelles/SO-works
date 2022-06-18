import matplotlib.pyplot as plt

from config import run_config, rm_files
#run_config()


def media_dos_tempos_medios(file:str)->float:
    soma=0
    with open(file, "r") as file:
        for readline in file: 
            line_strip = readline.strip()
            soma += float(line_strip)

    result = soma/10
    return result

def variancia_dos_tempos_medios(file:str, media:float)->float:
    soma=0
    count=0
    with open(file, "r") as file:
        for readline in file: 
            count+=1
            line_strip = readline.strip()
            soma = soma + (float(line_strip) - media) ** 2

    result = soma/count
    return result
"""
Média do Round Robin
"""

media_rr_50_p = media_dos_tempos_medios("escalonador_rr/resultado1.txt")
media_rr_100_p = media_dos_tempos_medios("escalonador_rr/resultado2.txt")
media_rr_150_p = media_dos_tempos_medios("escalonador_rr/resultado3.txt")
media_rr_200_p = media_dos_tempos_medios("escalonador_rr/resultado4.txt")
media_rr_250_p = media_dos_tempos_medios("escalonador_rr/resultado5.txt")

arrayRR = [media_rr_50_p, media_rr_100_p, media_rr_150_p, media_rr_200_p, media_rr_250_p]

"""
Variância do Round Robin
"""
variancia_rr_50_p=variancia_dos_tempos_medios("escalonador_rr/resultado1.txt", media_rr_50_p)
variancia_rr_100_p=variancia_dos_tempos_medios("escalonador_rr/resultado2.txt", media_rr_100_p)
variancia_rr_150_p=variancia_dos_tempos_medios("escalonador_rr/resultado3.txt", media_rr_150_p)
variancia_rr_200_p=variancia_dos_tempos_medios("escalonador_rr/resultado4.txt", media_rr_200_p)
variancia_rr_250_p=variancia_dos_tempos_medios("escalonador_rr/resultado5.txt", media_rr_250_p)


"""
Média do de Prioridades
"""
media_prio_50_p = media_dos_tempos_medios("escalonador_prio/resultado1.txt")
media_prio_100_p = media_dos_tempos_medios("escalonador_prio/resultado2.txt")
media_prio_150_p = media_dos_tempos_medios("escalonador_prio/resultado3.txt")
media_prio_200_p = media_dos_tempos_medios("escalonador_prio/resultado4.txt")
media_prio_250_p = media_dos_tempos_medios("escalonador_prio/resultado5.txt")

arrayPRIO = [media_prio_50_p, media_prio_100_p, media_prio_150_p, media_prio_200_p, media_prio_250_p]

"""
Variância do Prioridades
"""
variancia_prio_50_p=variancia_dos_tempos_medios("escalonador_prio/resultado1.txt", media_prio_50_p)
variancia_prio_100_p=variancia_dos_tempos_medios("escalonador_prio/resultado2.txt", media_prio_100_p)
variancia_prio_150_p=variancia_dos_tempos_medios("escalonador_prio/resultado3.txt", media_prio_150_p)
variancia_prio_200_p=variancia_dos_tempos_medios("escalonador_prio/resultado4.txt", media_prio_200_p)
variancia_prio_250_p=variancia_dos_tempos_medios("escalonador_prio/resultado5.txt", media_prio_250_p)

"""
Média do FIFO
"""
media_fifo_50_p = media_dos_tempos_medios("escalonador_fifo/resultado1.txt")
media_fifo_100_p = media_dos_tempos_medios("escalonador_fifo/resultado2.txt")
media_fifo_150_p = media_dos_tempos_medios("escalonador_fifo/resultado3.txt")
media_fifo_200_p = media_dos_tempos_medios("escalonador_fifo/resultado4.txt")
media_fifo_250_p = media_dos_tempos_medios("escalonador_fifo/resultado5.txt")

arrayFIFO = [media_fifo_50_p, media_fifo_100_p, media_fifo_150_p, media_fifo_200_p, media_fifo_250_p]

"""
Variância do FIFO
"""

variancia_fifo_50_p=variancia_dos_tempos_medios("escalonador_fifo/resultado1.txt", media_fifo_50_p)
variancia_fifo_100_p=variancia_dos_tempos_medios("escalonador_fifo/resultado2.txt", media_fifo_100_p)
variancia_fifo_150_p=variancia_dos_tempos_medios("escalonador_fifo/resultado3.txt", media_fifo_150_p)
variancia_fifo_200_p=variancia_dos_tempos_medios("escalonador_fifo/resultado4.txt", media_fifo_200_p)
variancia_fifo_250_p=variancia_dos_tempos_medios("escalonador_fifo/resultado5.txt", media_fifo_250_p)


"""
Média do SJF
"""
media_sjf_50_p = media_dos_tempos_medios("escalonador_sjf/resultado1.txt")
media_sjf_100_p = media_dos_tempos_medios("escalonador_sjf/resultado2.txt")
media_sjf_150_p = media_dos_tempos_medios("escalonador_sjf/resultado3.txt")
media_sjf_200_p = media_dos_tempos_medios("escalonador_sjf/resultado4.txt")
media_sjf_250_p = media_dos_tempos_medios("escalonador_sjf/resultado5.txt")

arraySJF = [media_sjf_50_p, media_sjf_100_p, media_sjf_150_p, media_sjf_200_p, media_sjf_250_p]

"""
Variância do SJF
"""
variancia_sjf_50_p=variancia_dos_tempos_medios("escalonador_sjf/resultado1.txt", media_sjf_50_p)
variancia_sjf_100_p=variancia_dos_tempos_medios("escalonador_sjf/resultado2.txt", media_sjf_100_p)
variancia_sjf_150_p=variancia_dos_tempos_medios("escalonador_sjf/resultado3.txt", media_sjf_150_p)
variancia_sjf_200_p=variancia_dos_tempos_medios("escalonador_sjf/resultado4.txt", media_sjf_200_p)
variancia_sjf_250_p=variancia_dos_tempos_medios("escalonador_sjf/resultado5.txt", media_sjf_250_p)

"""
    Apagando o arquivo de resultado e escalonador
"""
rm_files()


"""
    Plot do gráfico TEMPO MÉDIO TOTAL
"""
# Using Numpy to create an array X
X = [50, 100, 150, 200, 250]

# Assign variables to the y axis part of the curve
a = arrayFIFO
b = arrayPRIO
c = arrayRR
d = arraySJF


# Plotting both the curves simultaneously
plt.plot(X, a, color='r', label='FIFO')
plt.plot(X, b, color='g', label='PRIO')
plt.plot(X, c, color='b', label='RR')
plt.plot(X, d, color='y', label='SJF')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Número de processos")
plt.ylabel("Tempo médio")
plt.title("Gráfico de tempo médio dos escalonadores")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()


