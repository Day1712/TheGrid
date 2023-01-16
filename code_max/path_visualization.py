import matplotlib.pyplot as plt


xs = []
ys = []
y = 0

for i in range (1,10):
    x = i
    xs.append(x)
    ys.append(y)
    y += 2

plt.plot(xs, ys, 'b-')
plt.show()
