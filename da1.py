import numpy as np
import pandas as pd

data = pd.read_csv("datasets/HousingData.csv")
data.head()
data.isnull().sum()
data.dropna(inplace=True)
data.head()

data.isnull().sum()

print("The shape of the data is: ")
data.shape

# Define the independent and dependent variables from the dataset
X = data.drop("MEDV", axis=1)
y = data["MEDV"]

# Splitting data into traing and testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Importing LinearRegression() function
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler
model = LinearRegression()
model.fit(X_train, y_train)

model.score(X_test,y_test)

test_predictions = model.predict(X_test)
test_predictions

test_predictions.mean()

data['MEDV'].mean()

campaign = [[0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1,296,15.3,396.90,4.98]]
model.predict(campaign)

help(train_test_split)