# With Basic Optimizations:
# Data: 48315632 Calculations (35 Terms) (-35 Calculations)
# Code: 12 Lines (without counters) (-11 lines)
# Time: 4.3868 Seconds (-5.4527sec)
import time
start = time.time()

nterms = 35
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
end = time.time()
print('Time taken for program: ', end - start)