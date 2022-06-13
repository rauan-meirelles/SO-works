#bin/bash
for i in 1 2 3 4 5 6 7 8 9 10; do
	./escalonador 50 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado1.txt
	./escalonador 100 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado2.txt
	./escalonador 150 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado3.txt
	./escalonador 200 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado4.txt
	./escalonador 250 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado5.txt

done
# soma=0
# while read line; do 
# 	soma = soma + $((line))
# done < resultado.txt
