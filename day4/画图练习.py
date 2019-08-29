import random
from matplotlib import pyplot as plt

a = [random.randint(20, 35) for i in range(120)]
b = range(0, 120)

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(b, a)

k = [i for i in range(1, 120)]
plt.xticks(b)
plt.show()
