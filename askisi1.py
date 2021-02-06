import numpy as np
import random
a = int(input("Parakalw eisagetai th diastash tou tetragwnou (akeraios arithmos):"))
while(a<=0):
    a = int(input("H diastash tou tetragwnou prepei na einai megaluterh tou 0:"))
if(a<4):
    print("H diastash tou tetragwnou einai mikroterh tou 4. Ara den yparxoun tetrades.")
lista = []

for i in range(a):
    lista.append([])
    for z in range(a):
        lista[i].append(0)
d = np.array(lista) 


theseis = a*a 
mises = theseis/2 
if isinstance(mises,float): 
   mises = int(mises)+1

total = 0 
for x in range(0,100):
       
    d = np.array(lista)
    for i in range(mises):
        n = random.randint(0,a-1)
        z = random.randint(0,a-1)
        while(d[n][z]==1):
            n = random.randint(0,a-1)
            z = random.randint(0,a-1)
        d[n][z] = 1

    number = 0 
    #katheta
    for i in range(a-3):
        for z in range(a):
            if(d[i][z] == 1 and d[i+1][z]==1 and d[i+2][z]==1 and d[i+3][z]==1):
                number += 1    
           
    #orizontia
    for i in range(a):
        for z in range(a-3):
            if(d[i][z] == 1 and d[i][z+1]==1 and d[i][z+2]==1 and d[i][z+3]==1):
                number += 1

    #diagwnia apo panw-aristera pros katw-deksia
    for i in range(a-3):
        for z in range(a-3):
            if(d[i][z] == 1 and d[i+1][z+1]==1 and d[i+2][z+2]==1 and d[i+3][z+3]==1):
                number += 1

    #diagwnia apo katw-aristera pros panw-deksia
    for i in range(3,a):
        for z in range(a-3):
            if(d[i][z] == 1 and d[i-1][z+1]==1 and d[i-2][z+2]==1 and d[i-3][z+3]==1):
                number += 1
    total += number
    
mesos_oros = total/100
print("Mesos oros tetradwn: "+ str(mesos_oros))
