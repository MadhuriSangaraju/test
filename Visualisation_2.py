import matplotlib.pyplot as plt

# Bar Graph
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Bar-One")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Bar-Two", color="g")
plt.legend()
plt.xlabel("bar no.")
plt.ylabel("bar height")
plt.title("Bar Graph")
plt.show()

# Histogram
ages = [22, 55, 62, 45, 21, 22, 34, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 48]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Histogram")
plt.legend()
plt.show()

# Scatter Plot
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# Stack Plot

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()

# Pie Chart

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow= True, explode=(0,0.1,0,0), autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
