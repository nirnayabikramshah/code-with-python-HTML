import matplotlib.pyplot as plt
size =[10,30,40,20]
labels = ["Python", "Java", "C++", "Ruby"]
plt.plot(size, labels=labels, autopct="%.1f%%")
plt.show()