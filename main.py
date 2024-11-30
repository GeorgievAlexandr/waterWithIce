import matplotlib.pyplot as plt
waterC = 4200
volumeSum = 0.2
waterVolume = 0.1
waterTemperature = 90
waterP = 1
iceP = 0.92
iceLambda = 333000
x = []
y = []
def calculateTemperature(t1, m1, m2):
    sumQ = m1 * waterC * t1
    afterQ = sumQ - m2 * iceLambda
    return afterQ / ((m1 + m2) * waterC)

for iteration in range(10):
    waterTemperature = calculateTemperature(waterTemperature, waterVolume * waterP, (volumeSum - waterVolume) * iceP)
    waterVolume = waterVolume + iceP/waterP * (volumeSum - waterVolume)
    x.append(iteration)
    y.append(waterTemperature)
plt.plot(x, y)
plt.xlabel("Итерация")
plt.ylabel("Температура")
plt.show()