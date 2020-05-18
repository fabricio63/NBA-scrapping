import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data\dataframe_NBA.csv")

data.plot(kind='scatter',x='Simple Rating System',y='Wins',color='red')
plt.savefig(r'static\scatter.png')

data.plot(kind='bar',x='Teams',y='Wins',color='blue')
plt.savefig(r'static\bar.png')

data.plot(kind='scatter',x='Opponent Points Per Game',y='Loss',color='red')
plt.savefig(r'static\scatter2.png')


