from matplotlib import pyplot as plt
import math

plt.xkcd()

x = list(range(-10, 11))
#y = [i**2 for i in x]
plt.plot(x,x, '-', label = 'linear')
#plt.plot(x,[i**2 for i in x], '-', label = 'squared')
#plt.plot(x,[i**3 for i in x], '-', label = 'cubed')
plt.plot(x, [10 * math.sin(i) for i in x], '-', label = 'sine')

plt.title('simple plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()


plt.show()
