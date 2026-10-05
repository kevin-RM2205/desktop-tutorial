"""
Escribir un que calcule la suma 
de los "N" numeros naturales
por ejemplo si n=100,el programa 
calculara la suma del 1 al 100
"""
import time 
#maraca de tiempo 
timestamp_01 = time.time()
n = 100
total_sum = 0
# ciclo for
for number in range (1,n+1):
    total_sum =  total_sum + number
    #: linea de codigo <- 0+1
    #suma = 1
    #2: sum<- 1 + 2
    #suma = 3
print(f"La suma de 1 hasta {n} es : {total_sum}")

#Tomando el tiempo final
timestamp_02 =  time.time()

#Tomando el timepo del tiempo de ejecuicion
print(f"Timepo de ejecicion: {timestamp_02 - timestamp_01} segundos")
#Tomando el tiempo final
timestamp_02 =  time.time()

#Tomando el timepo del tiempo de ejecuicion
print(f"Timepo de ejecicion: {(timestamp_02 - timestamp_01) * 1e6:.2f}  µs")

#importar la biblioteca de tiempo

import time
#crea las variables para
#el problema
n = 100
the_sum = 0

#tomando el t1
timestamp_01 = time.time()
#iniciando ciclo while
while(n > 0):
    the_sum = the_sum + n #100 + 99 + 98 + .. + 1
    m = n - 1
    timestamo_02 = time.time()
    