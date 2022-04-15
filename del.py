import matplotlib.pyplot as plt
import math 

# how to calulate benfords law
x = [1,2,3,4,5,6,7,8]
y = []
for d in range(1,9):
    y.append(math.log(((1+d)/d),10))
    
plt.bar(x,y)
plt.show()