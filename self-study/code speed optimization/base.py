# Without Optimizations:
# Data: 48,315,667 Calculations (35 Terms)
# Code: 23 Lines
# Time: 9.8442 Seconds
import time
start = time.time()
calcnum = 0

def recur_fibo(n):
    global calcnum
    if n <= 1:
        calcnum += 1
        return n
    else:
        calcnum += 1
        return(recur_fibo(n-1) + recur_fibo(n-2))     

nterms = 35

fibo = []
for i in range(nterms):
    fibo.append(recur_fibo(i))
    calcnum += 1
    print(f"Calculation: {calcnum}")

fibostr = ""
for a in range(len(fibo)):
    fibostr += str(fibo[a]) + ", "
    calcnum += 1

print(fibostr)
print(f"Calculations: {calcnum}")
end = time.time()
print('Time taken for program: ', end - start)