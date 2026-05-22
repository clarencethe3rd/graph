import matplotlib.pyplot as plt
import numpy as np
import random
x = np.arange(1, 11)
y = np.random.randint(1,20,10)
#lineplot
'''plt.figure(figsize=(18,16))
plt.plot(x,y,"m--*",linewidth=3,label = "study score")
plt.title('graph')
plt.xlabel("jguhiuuh")
plt.ylabel("score")
plt.legend()
plt.show()'''
#multiple line plot
plt.plot(x,x**2,label = "x²")
plt.plot(x,x**3, label = "x³")
plt.legend()
plt.show()