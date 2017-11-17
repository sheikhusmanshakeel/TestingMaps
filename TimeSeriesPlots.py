import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.font_manager as font_manager


style.use('ggplot')
font_path = 'C:\Windows\Fonts\Arial.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=14)
title_font = {'fontname':'Arial', 'size':'25', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'20'}

filePathMonthly = 'C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\PoissonDataMonthly.csv'
filePathDaily = 'C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\PoissonDataDaily.csv'

dateparseMonthly = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
timeSeriesMonthly =  pd.read_csv(filePathMonthly, sep=',', parse_dates=[0], header=1,
                         names=['MonthYear','Index', 'Fat', 'Sanitary Products', 'Roots','Other','Total'],
                         date_parser=dateparseMonthly, index_col='MonthYear')
rolmeanMonthly = pd.rolling_mean(timeSeriesMonthly['Fat'], window=3)
rolstdMonthly = pd.rolling_std(timeSeriesMonthly['Fat'] ,window=3)
#print(rolmeanMonthly,rolstdDaily)
timeSeriesMonthly['Fat'].rolling(center=False,window=3)

plt.plot(timeSeriesMonthly['Fat'], color='r', marker='*',label='Fat Blockage Count')
plt.plot(rolmeanMonthly, color ='g', label='Rolling Mean')
plt.plot(rolstdMonthly,color='purple', label = 'Rolling Standard Deviation')
#plt.plot(timeSeriesMonthly['Roots'], color='g', marker='^')
#plt.plot(timeSeriesMonthly['Sanitary Products'], color='b', marker='o')
plt.title('Blockage trend for Fat', **title_font)
plt.xlabel('Month/Year', **axis_font)
plt.ylabel('Blockage Count', **axis_font)
plt.legend(prop=font_prop, numpoints=1)
plt.show()
plt.axes(**axis_font)


dateparseDaily = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
timeSeriesDaily = pd.read_csv(filePathDaily, sep=',', parse_dates=[0], header=1,
                         names=['Date','Index', 'Fat', 'Sanitary Products', 'Roots','Other','Total'],
                         date_parser=dateparseDaily, index_col='Date')
plt.plot(timeSeriesDaily['Fat'], color='r', marker='*')
plt.title('Blockage trend for Fat', **title_font)
plt.xlabel('Date', **axis_font)
plt.ylabel('Blockage Count', **axis_font)
plt.legend(prop=font_prop, numpoints=1)
plt.show()


plt.plot(timeSeriesDaily['Sanitary Products'], color='darkcyan', marker='*')
plt.title('Blockage trend for Sanitary Products', **title_font)
plt.xlabel('Date', **axis_font)
plt.ylabel('Blockage Count', **axis_font)
plt.legend(prop=font_prop, numpoints=1)
plt.show()

plt.plot(timeSeriesDaily['Roots'], color='purple', marker='*')
plt.title('Blockage trend for Roots', **title_font)
plt.xlabel('Date', **axis_font)
plt.ylabel('Blockage Count', **axis_font)
plt.legend(prop=font_prop, numpoints=1)
plt.show()

