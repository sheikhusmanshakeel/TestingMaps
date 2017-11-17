import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import chisqprob
from scipy.stats import chisquare
# %matplotlib inline
from os import listdir
from os.path import isfile, join

# Set the font path properly here if not using Windows. Otherwise just comment this out
plt.style.use('ggplot')
font_path = 'C:\Windows\Fonts\Arial.ttf'
font_prop = font_manager.FontProperties(size=12)
title_font = {'fontname': 'Arial', 'size': '15', 'color': 'black', 'weight': 'normal',
              'verticalalignment': 'bottom'}  # Bottom vertical alignment for more space
axis_font = {'fontname': 'Arial', 'size': '12'}


def GeneralizedLinearRegression(blockageData, dependentVariable, independentVariable, distributionFamily,
                                familyName, blockageName, graphFileName):
    print('GENERALIZED LINEAR REGRESSION - {0} Family, for {1}'.format(familyName, blockageName))
    formula = '{0}~{1}'.format(dependentVariable, independentVariable)
    model = smf.glm(formula=formula, data=blockageData, family=distributionFamily)
    fittedModel = model.fit()
    print('Deviance Residual', fittedModel.deviance)
    pearsonResiduals = fittedModel.resid_pearson
    devianceResiduals = fittedModel.resid_deviance
    pValue = chisqprob(fittedModel.deviance, fittedModel.df_resid)
    # H0 (null hypothesis) : Model correctly follows given distribution
    # H1 (alternative hypothesis): Model does not follow given distribution
    print('Chisquare value', pValue)
    if pValue > 0.05:
        print('Can NOT reject the null hypothesis. Model correctly follows {0} distribution.'.format(familyName))
    else:
        print('Reject the null hypothesis. Model does not follow {0} distribution'.format(familyName))
    print(fittedModel.summary())
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35]
    newValues = pd.DataFrame(x)
    newValues.columns = ['Index']
    predictedY = fittedModel.predict(newValues)
    labelObservedData = 'Observed Data - {0}'.format(blockageName)
    plt.figure(figsize=(10, 8), dpi=400)
    plt.scatter(blockageData['Index'], blockageData[blockageType], color='red', label=labelObservedData)
    plt.plot(predictedY, marker='o', color='purple', label='Fitted/Predicted')
    plt.xlabel('Index', **axis_font)
    plt.ylabel('Blockage Count', **axis_font)
    plt.legend(prop=font_prop, numpoints=1, loc='upper right')
    plt.savefig(graphFileName, dpi=400)
    plt.show()
    print('=========================================================================================================')
    print('=========================================================================================================')


# blockageTypes = ['TotalCount','SanitaryProductsCount','UnknownCount']
# blockageTypeNames = ['Total Blockages','Sanitary Products','Missing\\Unknown']

blockageTypes = ['TotalCount']
blockageTypeNames = ['Total Blockages']

folderLocationData20 = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\GridFiles"
folderLocationImages20 = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\Images\\GFiles"
onlyfiles = [f for f in listdir(folderLocationData20) if isfile(join(folderLocationData20, f))]
i = 0

for file in onlyfiles:
    completeFileGridAnalysis = '{0}\\{1}'.format(folderLocationData20, file)
    data = pd.DataFrame(pd.read_csv(completeFileGridAnalysis))
    for blockageType in blockageTypes:
        poifamily = sm.families.Poisson(sm.families.links.log)
        familyName = 'Poisson'
        GeneralizedLinearRegression(
            blockageData=data,
            dependentVariable=blockageType,
            independentVariable='Index',
            distributionFamily=poifamily,
            familyName=familyName,
            blockageName=blockageTypeNames[i],
            graphFileName='{0}{1}_{2}.png'.format(folderLocationImages20, file, blockageType))

        negativeBin = sm.families.NegativeBinomial()
        familyName = 'Negative Binomial'
        GeneralizedLinearRegression(
            blockageData=data,
            dependentVariable=blockageType,
            independentVariable='Index',
            distributionFamily=negativeBin,
            familyName=familyName,
            blockageName=blockageTypeNames[i],
            graphFileName='{0}{1}_{2}_{3}.png'.format(folderLocationImages20, file, blockageType, familyName))
        i += 1
