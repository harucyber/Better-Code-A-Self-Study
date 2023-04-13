# Base Code
# 15 Lines of Code (3-18)

location = "self-study/code simplification/assets"

import os
import time

start = time.time()

try:
    os.mkdir(location)
except FileExistsError:
    print("This folder already exists.")

print("Complete!")
end = time.time()
print('Time taken for program: ', end - start)

# Developer Tool: 
# os.remove(location)