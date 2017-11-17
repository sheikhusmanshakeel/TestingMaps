import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import chisqprob
from scipy.stats import chisquare

from os import listdir
from os.path import isfile, join


# Set the font path properly here if not using Windows. Otherwise just comment this out
plt.style.use('ggplot')
font_path = 'C:\Windows\Fonts\Arial.ttf'
font_prop = font_manager.FontProperties(size=12)
title_font = {'fontname':'Arial', 'size':'15', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Arial', 'size':'12'}

def ShowGraph(trends,labels,numberOfPlot):
    graphFileName = '{0}\\{1}_{2}.png'.format(folderLocationImages20,
                                                  blockageType,numberOfPlot)
    fig = plt.figure(figsize=(12, 8), dpi=400)
    ax = plt.subplot(111)
    i=0
    for trend in trends:
        ax.plot(trend, marker='o', label=labels[i])
        i += 1

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),
              fancybox=True, shadow=True, ncol=5)
    plt.xlabel('Month/Year', **axis_font)
    plt.ylabel('Blockage Count', **axis_font)
    plt.savefig(graphFileName, dpi=400)
    #plt.show()


# blockageTypes = ['TotalCount','SanitaryProductsCount','UnknownCount']
# blockageTypeNames = ['Total Blockages','Sanitary Products','Missing\\Unknown']
blockageTypes = ['TotalCount']
blockageTypeNames = ['Total Blockages']

folderLocationData20 = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\GridFiles"
folderLocationImages20 = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\Images\\GridFiles"

onlyfiles = [f for f in listdir(folderLocationData20) if isfile(join(folderLocationData20, f))]
dateparseMonthly = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
arrayOfTimeSeries = []
arrayOfLabels = []
i= 1
numberOfplots= 1
for blockageType in blockageTypes:
   for file in onlyfiles:
        completeFileGridAnalysis = '{0}\\{1}'.format(folderLocationData20, file)
        timeSeriesMonthly = pd.read_csv(completeFileGridAnalysis, sep=',', parse_dates=[1], header=1,
                                        names=['GridId', 'MonthYear', 'Index', 'Fat', 'Sanitary Products', 'Roots',
                                               'Other',
                                               'Unknown', 'TotalWithoutUnknown', 'Total'],
                                        date_parser=dateparseMonthly, index_col='MonthYear')
        arrayOfTimeSeries.append(timeSeriesMonthly['Total'])
        fileComponents = file.split('_')
        gridId = fileComponents[0][4:]
        lab = 'Grid - {0}'.format(gridId)
        arrayOfLabels.append(lab)
        if i == 7:
            ShowGraph(arrayOfTimeSeries,arrayOfLabels,numberOfPlot=numberOfplots)
            arrayOfLabels = []
            arrayOfTimeSeries = []
            i=0
            numberOfplots +=1
        i +=1


ShowGraph(arrayOfTimeSeries,arrayOfLabels,numberOfPlot=numberOfplots)



