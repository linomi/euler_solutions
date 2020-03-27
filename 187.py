import math 
import pickle
m = open("test.txt", "a")
def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
def primes(num):
    #m.write("[")
    primes = []
    for i in range(2,int(num)+1):
        if is_prime(i)== True:
            #m.write(str(i)+",")
            primes.append(i)
    #m.write("]")    
    #m.close
    return primes
m = 10**8#int(input("vared kon"))
x = primes(m/2)
y = len(x)
sum= 0 
for element in x:
    for element2  in reversed(x):
        
        if element*element2<m:
            x = x[ :x.index(element2)+1]
            sum += len(x)
            x = x[1:] 
            break
print(sum)
    
