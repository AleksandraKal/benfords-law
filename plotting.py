import matplotlib.pyplot as plt
import math 

# how to calulate benfords law
x = [1,2,3,4,5,6,7,8,9]
y = []
for d in range(1,10):
    y.append(math.log(((1+d)/d),10) * 100)
z = [47.2, 23.6, 17.6, 6.0, 0.4, 0.8, 0.4, 0.4, 0.8]

plt.bar(x,z, color='grey')
plt.plot(x,y,linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
plt.title("Benford Test")
plt.xlabel('Leading digit')
plt.ylabel("Percentage")
plt.legend(["Observed distrubiton", "Benford distrubution"])
plt.show()

