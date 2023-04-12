# With Standard Optimizations: Instead of Recursive, Iterative Programming 
# Data: 13 Calculations (15 Terms) (-48315619 Calculations)
# Code: 8 lines (without calculations) (-4 Lines)
# Time: 0 Seconds (-4.38sec)
import time
start = time.time()
nterms = 15
calculate = 0
fib_seq = [0, 1]
fib_str = ""
for i in range(nterms-2):
    calculatedvalue = (fib_seq[i] + fib_seq[i+1])
    fib_seq.append(calculatedvalue)
    fib_str += str(calculatedvalue) + ", "
    calculate += 1
print(fib_str)
print(f"Calculations: {calculate}")
end = time.time()
print('Time taken for program: ', end - start)