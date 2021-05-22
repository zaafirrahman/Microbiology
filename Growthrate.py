import matplotlib.pyplot as plt
import math

stop = False
y = []
l = 0

while (not stop) :
  pT = float(input("Input %T in {} hour(s) or '0' to end : ".format(l)))
  if pT != 0 :
    od = (2 - math.log(pT,10))
    print('Optical Density (OD) in {} hour(s) : {:.3f}'.format(l,od))
    print('-'*42)
    y.append(od)
    l += 1
  else :
    stop = True

x = list(range(l))

fig, ax = plt.subplots()

ax.plot(x, y, 'ro-')
ax.set(ylabel = 'Optical Density', xlabel = 'Time')
ax.set(title = 'Kurva Pertumbuhan Mikroba')
ax.legend(['OD Value'])
ax.grid()

plt.show()
