import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel('天气.xlsx')
x = df['日期']
y = df['温度']
plt.plot(x,y)
plt.show()