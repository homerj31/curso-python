import time
inicio = time.time()
print (inicio)

for num in range (0,10000000):
    print (num)
    

fin = time.time()
print (fin - inicio)
