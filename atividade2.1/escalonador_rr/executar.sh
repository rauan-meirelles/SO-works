#bin/bash
for i in 1 2 3 4 5 6 7 8 9 10; do
	./escalonador 5 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado.txt

done
soma=0
while read line; do 
	soma = soma + $((line))
done < resultado.txt
