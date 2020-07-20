# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:28:14 2020

@author: Meghana
"""


#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math
import seaborn as sns


#importing the dataset
dataset2017=pd.read_csv('2017.csv')
datasetppl=pd.read_csv('POPULATION.csv')
datasetregion=pd.read_csv('region.csv')
dataset2017=dataset2017.iloc[0:50,:]
datasetleast=pd.read_csv('2017.csv')
datasetleast=datasetleast.iloc[145:155,:]

dataset2017 = pd.concat([dataset2017, datasetleast]).reset_index(drop=True)


dataset2017['region']="region"
dataset2017['population']="population"

for i in range(0,60):
    print(i)
    if i==32:
        continue
    if i==39:
        continue
    if i==48:
        continue
    if i==49:
        continue
    if i==50:
        continue
    if i==51:
        continue
    if i==56:
        continue
    
    country=dataset2017['Country'][i]
    index=datasetregion[datasetregion['Country'] ==country].index[0]
    dataset2017['region'][i]=datasetregion['Region'][index]
    indexppl=datasetppl[datasetppl['Country Name'] ==country].index[0]
    dataset2017['population'][i]=datasetppl['POPULATION'][index]



import matplotlib.pyplot as plt
#line chart of life expectancy for all countries

plt.figure(figsize=(30,5))
plt.plot(dataset2017['Country'],dataset2017['Health..Life.Expectancy.'])
plt.title('life expectancy vs country')
plt.xlabel('country')
plt.ylabel('life expectancy')
plt.show()

#line chart of population size for all countries
plt.plot(dataset2017['Country'],dataset2017['population'])
plt.title('population vs country')
plt.xlabel('country')
plt.ylabel('population')
plt.show()

#bar graph of regions versus life expectancy
sns.barplot(x="Health Life Expectancy", y="region", data=dataset2017, palette='Accent')

#Calculate Correlation and linear regression between: 
#Happiness and life expectancy and Happiness and population


final=pd.read_csv('final.csv')
dataset2017['Happiness.Score'].corr(dataset2017['Health..Life.Expectancy.'])
#correlation=0.9071593037651688
x=dataset2017['population'].values
final['Happiness.Score'].corr(final['population'])
#correlation=0.011697205134169629

y=final.loc[:,'Happiness.Score'].values
x=final.loc[:,'Health..Life.Expectancy.'].values
x=x.reshape(-1,1)
y=y.reshape(-1,1)
#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y, test_size=0.2, random_state=0)



# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
y_predict=regressor.predict(X_test)

#Visualizing the training set results
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train),color='green')
plt.title('life exp vs hap(TRAINING SET)')
plt.xlabel('life exp')
plt.ylabel('hap')
plt.show()

y=final.loc[:,'Happiness.Score'].values
x=final.loc[:,'population'].values
x=x.reshape(-1,1)
y=y.reshape(-1,1)
#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y, test_size=0.2, random_state=0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
y_predict=regressor.predict(X_test)

#Visualizing the training set results
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train),color='green')
plt.title('happ n pop(TRAINING SET)')
plt.xlabel('pop')
plt.ylabel('hap')
plt.show()




