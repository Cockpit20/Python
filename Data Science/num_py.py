import time
import numpy as np

x = np.random.rand(10000000)

start = time.time()
mean = sum(x)/len(x)
print(time.time() - start)

start = time.time()
mean_np = np.mean(x)
print(time.time() - start)