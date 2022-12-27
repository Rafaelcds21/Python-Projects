import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import optimize


def f(x, a, b):
    return x*a+b


table = pd.read_excel('Path of database')

x1 = table['x axis data']
y1 = table['y axis data']

guess = [1, 1]

params, params_covariance = scipy.optimize.curve_fit(f, x1, y1, guess)

a = params[0]
b = params[1]

print(f'Linear fit function: y = %.2f.x + %.2f' %(a, b))

plt.plot(x1, y1)
plt.title('Title of graphic')
plt.xlabel('Title of label x')
plt.ylabel('Title of label y')
plt.show()
