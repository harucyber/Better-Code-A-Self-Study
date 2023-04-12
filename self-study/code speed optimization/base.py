# Without Optimizations:
# Data: 3207 Calculations (15 Terms)
# Code: 23 Lines

calcnum = 0

def recur_fibo(n):
    global calcnum
    if n <= 1:
        calcnum += 1
        return n
    else:
        calcnum += 1
        return(recur_fibo(n-1) + recur_fibo(n-2))     

nterms = 15

fibo = []
for i in range(nterms):
    fibo.append(recur_fibo(i))
    calcnum += 1

fibostr = ""
for a in range(len(fibo)):
    fibostr += str(fibo[a]) + ", "
    calcnum += 1

print(fibostr)
print(f"Calculations: {calcnum}")