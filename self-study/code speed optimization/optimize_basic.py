# With Basic Optimizations:
# Data: 3192 Calculations (15 Terms) (-15 calculations)
# Code: 12 Lines (without counters) (-11 lines)


nterms = 15
counter = 0

def recur_fibo(n):
   global counter
   if n <= 1:
       counter += 1
       return n
   else:
       counter += 1
       return(recur_fibo(n-1) + recur_fibo(n-2))

recurfibo = ""
for i in range(nterms):
    counter += 1
    recurfibo += (str(recur_fibo(i)) + ", ")
print(recurfibo)
print(f"Calculations: {counter}")