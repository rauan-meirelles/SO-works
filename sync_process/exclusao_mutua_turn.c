#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

long conta = 0;
long turn = 1;
void * t1(){
    long i;
    for(i=0; i < 1000000; i++){
        while(turn!=1);
        
        conta = conta + 5;
        turn=2;
    }

    printf("Encerrei t1\n");
}

void * t2(){
    long i;
    for(i=0; i < 1000000; i++){
        while(turn!=2);
        conta = conta + 2;
        turn=1;
    }

    printf("Encerrei t2\n");
}


int main(){
    pthread_t tid1, tid2;
    pthread_create(&tid1, NULL, &t1, NULL);
    pthread_create(&tid2, NULL, &t2, NULL);

    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    printf("O valor da variável conta é: %ld\n", conta);
    return 0;
}