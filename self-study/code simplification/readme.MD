# Code Simplification
| Base | Abstraction |

```# Base Code
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
# os.remove(location)```

```# Base Code
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
# print("System Fail without Sudo. Please elevate this program.")```
|
