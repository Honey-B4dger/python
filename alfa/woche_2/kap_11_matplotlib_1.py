import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

x = np.linspace(0,10)
y = x**2

plt.figure(figsize= (7,5))
res = plt.subplot(2, 1, 1)

print(res)

plt.plot(x,x, '.')

plt.title('Subplot usage')
plt.grid(color = 'black', alpha = 0.8, linestyle = '-', linewidth = 0.5)
plt.subplot(2,1,2)

plt.plot(x, x**2, '--')

plt.grid(color = 'black', alpha = 0.8, linestyle = '-', linewidth = 0.5)

plt.show()


