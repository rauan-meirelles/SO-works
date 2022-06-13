#import matplotlib.pyplot as plt

from config import run_config, rm_files
run_config()


def media_dos_tempos_medios(file:str)->int:
    soma=0
    with open(file, "r") as file:
        for readline in file: 
            line_strip = readline.strip()
            soma += float(line_strip)

    result = soma/10
    return result
"""
Média do Round Robin
"""
media_rr_50_p = media_dos_tempos_medios("escalonador_rr/resultado1.txt")
media_rr_100_p = media_dos_tempos_medios("escalonador_rr/resultado2.txt")
media_rr_150_p = media_dos_tempos_medios("escalonador_rr/resultado3.txt")
media_rr_200_p = media_dos_tempos_medios("escalonador_rr/resultado4.txt")
media_rr_250_p = media_dos_tempos_medios("escalonador_rr/resultado5.txt")


"""
Média do de Prioridades
"""
media_prio_50_p = media_dos_tempos_medios("escalonador_prio/resultado1.txt")
media_prio_100_p = media_dos_tempos_medios("escalonador_prio/resultado2.txt")
media_prio_150_p = media_dos_tempos_medios("escalonador_prio/resultado3.txt")
media_prio_200_p = media_dos_tempos_medios("escalonador_prio/resultado4.txt")
media_prio_250_p = media_dos_tempos_medios("escalonador_prio/resultado5.txt")

"""
Média do FIFO
"""
media_fifo_50_p = media_dos_tempos_medios("escalonador_fifo/resultado1.txt")
media_fifo_100_p = media_dos_tempos_medios("escalonador_fifo/resultado2.txt")
media_fifo_150_p = media_dos_tempos_medios("escalonador_fifo/resultado3.txt")
media_fifo_200_p = media_dos_tempos_medios("escalonador_fifo/resultado4.txt")
media_fifo_250_p = media_dos_tempos_medios("escalonador_fifo/resultado5.txt")


"""
Média do SJF
"""
media_sjf_50_p = media_dos_tempos_medios("escalonador_sjf/resultado1.txt")
media_sjf_100_p = media_dos_tempos_medios("escalonador_sjf/resultado2.txt")
media_sjf_150_p = media_dos_tempos_medios("escalonador_sjf/resultado3.txt")
media_sjf_200_p = media_dos_tempos_medios("escalonador_sjf/resultado4.txt")
media_sjf_250_p = media_dos_tempos_medios("escalonador_sjf/resultado5.txt")

"""
    Apagando o arquivo de resultado e escalonador
"""
rm_files()


# """
# Mostrando a média
# """
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()