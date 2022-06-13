import os
def run_config():
    

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

def rm_files():
    """
    Apagando o arquivo de resultado e escalonador
    """
    os.system("cd escalonador_prio && rm resultado1.txt && rm escalonador")
    os.system("cd escalonador_prio && rm resultado2.txt")
    os.system("cd escalonador_prio && rm resultado3.txt")
    os.system("cd escalonador_prio && rm resultado4.txt")
    os.system("cd escalonador_prio && rm resultado5.txt")

    os.system("cd escalonador_fifo && rm resultado1.txt && rm escalonador")
    os.system("cd escalonador_fifo && rm resultado2.txt")
    os.system("cd escalonador_fifo && rm resultado3.txt")
    os.system("cd escalonador_fifo && rm resultado4.txt")
    os.system("cd escalonador_fifo && rm resultado5.txt")


    os.system("cd escalonador_rr && rm resultado1.txt && rm escalonador")
    os.system("cd escalonador_rr && rm resultado2.txt")
    os.system("cd escalonador_rr && rm resultado3.txt")
    os.system("cd escalonador_rr && rm resultado4.txt")
    os.system("cd escalonador_rr && rm resultado5.txt")


    os.system("cd escalonador_sjf && rm resultado1.txt && rm escalonador")
    os.system("cd escalonador_sjf && rm resultado2.txt")
    os.system("cd escalonador_sjf && rm resultado3.txt")
    os.system("cd escalonador_sjf && rm resultado4.txt")
    os.system("cd escalonador_sjf && rm resultado5.txt")
