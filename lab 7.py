import numpy
import random
import time
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FuncAnimation

# Задание 1
data1 = []
data2 = []
for i in range(1000000):
    data1.append(random.randint(1, 100))
    data2.append(random.randint(1, 100))

data1_py = data1
data2_py = data2
data1_num = numpy.array(data1)
data2_num = numpy.array(data2)

time1 = time.perf_counter()

for j in range(1000000):
    data2_py[j] = data1_py[j] * data2_py[j]

time1_ans = time.perf_counter() - time1

time2 = time.perf_counter()

new_data = numpy.multiply(data1_num, data2_num)

time2_ans = time.perf_counter() - time2

print('Задание 1:')
print("Время перемножения питоновских списков:", time1_ans)
print("Время перемножения NumPy массивов:", time2_ans)

if time1_ans > time2_ans:
    print('Убедился, что библиотека NumPy имеет очень быстрые алгоритмы работы с массивами')

# Задание 2

t = []
p = []
ch = []
with open('data1.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table)[1:]:
        t.append(float(row[0]))
        p.append(int(row[3]))
        ch.append(float(row[17]))

t = numpy.array(t, float)
p = numpy.array(p, float)
ch = numpy.array(ch, float)

fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set(title='Зависимости от времени', xlabel='Время, с', ylabel='Положение дроссельной заслонки (%)')
ax1.plot(t, p, color='pink')
ax1.legend('1')

ax2 = ax1.twinx()
ax2.set(ylabel='Часовой расход топлива (л\час)')
ax2.plot(t, ch, color='green')
ax2.legend('2')

n = numpy.random.normal(0, 0.3, size=len(p))
p_jitter = p + n

fig2 = plt.figure()
ax3 = fig2.add_subplot()
ax3.set(title='График корреляции', xlabel='Положение дроссельной заслонки (%)', ylabel='Часовой расход топлива (л\час)')
ax3.plot(p_jitter, ch, 'o', alpha=0.3, markersize = 4)
plt.show()

# Задание 3
x = numpy.linspace(numpy.pi * (-5), numpy.pi * (5))
y = numpy.cos(x)
z = numpy.sin(x)

figure = plt.figure()
ax1 = figure.add_subplot(111, projection='3d')
ax1.plot(x, y, z, color='salmon')
plt.show()

# Доп. задание
def sin(i):
    line.set_ydata(numpy.sin(x + i / 10.0))
    return line,


x = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(x)
fig, ax1 = plt.subplots()
line, = ax1.plot(x, y,  color='green')

animate = FuncAnimation(fig, sin, frames=100, interval=50)
plt.show()

writer = PillowWriter(fps=25)
animate.save("sin.gif", writer=writer)