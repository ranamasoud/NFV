# -*- coding: utf-8 -*-
"""ranaMasoud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vsm5CdOpV-MkVflM60yzYBPdGchqeZAk

# Resource Management and Optimisation in Network Function Virtualisation (NFV) Environments Using Python-Based Solutions
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split #s
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

#Loading Data
train_dataset = pd.read_csv('/content/UNSW_NB15_training-set.csv')
test_dataset = pd.read_csv('/content/UNSW_NB15_testing-set.csv', encoding='latin-1')

train_dataset.head()

test_dataset.head()

train_dataset["label"].value_counts()

train_dataset.info()

test_dataset.info()

test_dataset.drop(columns=['attack_cat','proto','service','state'],axis=1,inplace=True)
train_dataset.drop(columns=['attack_cat','proto','service','state'],axis=1,inplace=True)

train_dataset.isna().sum()

test_dataset.isna().sum()

plt.figure(figsize=(20,20))
sns.heatmap(train_dataset.corr(),annot=True)
plt.show()

#EDA
sns.countplot(y="label", data=train_dataset)
plt.show()

X=train_dataset.drop('label',axis=1)
y=train_dataset['label']

lr=LinearRegression()

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=101, test_size=0.2)

lr.fit (X_train,y_train)

prediction = lr.predict(X_test)

testaccuracy = lr.score(X_test,y_test)
print(testaccuracy)

"""We achived the accuracy of 74% from Linear Regression Model.

"""

model_gradient = GradientBoostingClassifier(n_estimators=100, random_state=101)

predictions_gbc = model_gradient.fit(X_train, y_train).predict(X_test)

accuracy_gbc = accuracy_score(y_test, predictions_gbc)
print("Accuracy:", accuracy_gbc)

"""Gradient Booster Classification is an Example of emsemble learning and by using that model had achived accuracy of 98.0% which signifies that the model is predicting acurately."""

plt.figure(figsize=(7, 7))
plt.title('Predicted vs Actual Values')
plt.scatter(y_test, predictions_gbc)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.show()

"""The Graph Shows that our model is giving accurate predictions. As the acutal and predicted values are same."""