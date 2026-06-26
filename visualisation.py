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

#bar chart 
plt.bar([1,3,5,7,9],[10,15,12,30,25], label = "qopwkf")
plt.bar([2,4,6,8,10],[5,25,14,20,35], label = "dqw")
plt.legend()
plt.show()
#bar chart with catogorical values
plt.bar(["apple","orange"],[10,15], label = "qopwkf")
plt.show()

#histogram
ages = np.random.randint(10,60,50)
print(ages)
intervals = np.arange(10,61,5)
plt.hist(ages, intervals)
plt.show()

#scatter plot
x = np.arange(1,6)
y = np.random.randint(10,20,5)
plt.scatter(x,y,color = "red", marker="*",s=25)
plt.show()

#pie chart
act = ["sleep","school","eat","play","others"]
hours = [10,7,1,3,3]
plt.pie(hours,labels=act,autopct="%1.0f%%",startangle=90,colors=["red","blue","purple","green","orange"],shadow=True)
plt.show()

#stack plot
monday = [7,8,7,9,10]
tuesday = [6,10,2,3,5]
wednesday= [7,7,4,3,6]
thursday= [10,2,5,6,3]
friday= [7,6,2,10,4]
plt.stackplot(act,monday,tuesday,wednesday,thursday,friday,labels=["mon","tue","wed","thur","fri"])
plt.legend()
plt.show()
#subplots
plt.figure(figsize=(20,8))
plt.subplot(2,3,4)
plt.pie(hours,labels=act,autopct="%1.0f%%",startangle=90,colors=["red","blue","purple","green","orange"],shadow=True)
plt.subplot(2,3,2)
plt.scatter(x,y,color = "red", marker="*",s=25)
plt.show()
