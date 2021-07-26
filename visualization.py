import pandas as pd
df = pd.read_csv('salaries.csv')

from matplotlib import pyplot
pyplot.plot(df['Age'], df['Salary'])
# pyplot.scatter(df['Age'], df['Salary'])
pyplot.show()
