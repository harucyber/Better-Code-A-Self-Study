# Base Code
# 12 Lines of Code (3-15)
import os
import time

start = time.time()

try:
    os.mkdir("self-study/code simplification/assets")
except FileExistsError:
    print("This folder already exists.")

print("Complete!")
print('Time taken for program: ', time.time() - start)
# Developer Tool: 
# try:
# os.remove("self-study/code simplification/assets")
# except PermissionError:
# print("System Fail without Sudo. Please elevate this program.")