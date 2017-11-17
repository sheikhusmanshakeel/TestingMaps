import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
from scipy.stats import chisquare
from scipy.stats.distributions import poisson as p



filePathMonthly = 'C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\PoissonDataMonthly.csv'
filePathDaily = 'C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\PoissonDataDaily.csv'

#x=np.array([2.0,19.0,28.0,232.0,271.0])
#y=np.array([1,2,3,4,5])
#poisson = sm.families.Poisson
#poisson.starting_mu(y)
#model = smf.poisson(endog=x,exog=y, family=poisson)
#fittedBFGS = model.fit(method='bfgs').resid
#print(fittedBFGS.summary2())


data= pd.DataFrame(pd.read_csv(filePathMonthly))
modFat = smf.poisson('FatCount~Index', data=data).fit(method='bfgs')
residual = modFat.resid
#plt.plot(modFat.fittedvalues)
#plt.show()
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

newValues = pd.DataFrame(x)
Y = modFat.predict(x)

#print(modFat.params)
#print(modFat.tvalues)
#print(modFat.mu)
print(residual)
#print(modFat.summary())

dataF= np.array(data['FatCount'])
endog = np.ones_like(dataF)
res = sm.Poisson(dataF,endog).fit()
#print(res.summary())
#print(res.predict())


print(res.resid)







