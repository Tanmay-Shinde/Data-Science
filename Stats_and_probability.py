from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics

data = [255, 259, 264, 270, 276, 278, 282, 296, 297, 304, 306, 309, 309, 317, 323, 327, 330, 330, 333, 334, 342, 349,
        350, 351, 353, 358, 362, 364, 367, 376, 377, 383, 384, 385, 385, 391, 391, 393, 394, 398, 404, 406, 408, 411,
        416, 423, 424, 430, 435, 437, 437, 439, 440, 446, 450, 450, 462, 466, 478, 482, 482, 501, 503, 516, 525, 529,
        529, 530, 550, 552, 558, 581, 595, 628, 673, 760, 834]

mean = statistics.mean(data)
print("Mean = ",mean)
sd = statistics.stdev(data)
print("Standard deviation = ", sd)

plt.title('Housing expenses probability distribution')
plt.xlabel('X-axis (Housing Expenses)')
plt.ylabel('Y-axis (Probability density function)')

plt.plot(data, norm.pdf(data, mean, sd))
plt.show()

#x_axis = [0, 1, 2, 2, 5, 5, 5, 10, 10, 12]
#y_axis =[19, 20, 22, 24, 25, 26, 28, 29, 32, 34]

#x = np.array(x_axis)
#y = np.array(y_axis)

#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m*x+b)

#plt.scatter(x_axis, y_axis, s = 30)
#plt.show()
