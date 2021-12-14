import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def calc_possibilities(num_backwards, pos, num):
    if (num_backwards < 0):
        return 0
    elif (num_backwards > 0 and pos == 0):
        return 0
    elif (2 + num < pos):
        return 0
    
    if (pos != 0):
        return calc_possibilities(num_backwards - 1, pos + 1, num) + calc_possibilities(num_backwards, pos - 1, num)
    elif (num_backwards == 0 and pos == 0):
        return 1
        

num_backwards = 6

def catalan(i):
    prod = 1
    if (i == 2):
        return 2
    if (i > 2):
        for j in range(2, i+1):
            temp = (j+i)/j
            prod *= temp
    return prod

print(catalan(4))
print(calc_possibilities(1, 2, 1))

         

y = []
attacking_ratio = 10/100
sum = 0

ratios = [.05, .1, .25, .5]
j = 3
for i in range(101): 
        per = catalan(i) * (ratios[j])**(i+2) * (1 - ratios[j])**(i)
        sum += per
        y.append(sum)

x = np.linspace(0, 100, 101)

plt.plot(x, y)
plt.xlabel("Block Tolerance", font = {'size' : 10})
plt.ylabel("Success Probability", font = {'size' : 10})
plt.title("Attacking Computation: k/N = {}".format(ratios[j]), font = {'size' : 15})
plt.savefig('general_attack_prob.png')
plt.show()

"""

for j in range(len(ratios)):
    ax = plt.subplot(2, 2, j + 1)
    y =[]
    sum = 0
    for i in range(101): 
        per = catalan(i) * (ratios[j])**(i+2) * (1 - ratios[j])**(i)
        sum += per
        y.append(sum)
    
    x = np.linspace(0, 100, 101)
    ax.ticklabel_format(useOffset=False)
    ax.plot(x, y)
    ax.set_xticklabels(x, fontsize=5)
    ax.set_yticklabels(x, fontsize=5)
    ax.set_xlabel("Block Tolerance", font = {'size' : 7})
    ax.set_ylabel("Success Probability", font = {'size' : 7})
    ax.set_title("Attacking Computation: k/N = {}".format(ratios[j]), font = {'size' : 9})

plt.tight_layout()
plt.savefig('general_attack_prob.png')
plt.show()
"""