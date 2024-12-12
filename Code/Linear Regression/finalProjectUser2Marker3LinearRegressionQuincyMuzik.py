# Final Project User 2 Marker 3 Linear Regression by Quincy Muzik 12/11/2024

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the CSV File with custom parameters
dfMocapData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv',nrows=1)

# Load the CSV with additional parameters 
dfMocapData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv', skiprows=range(2,5225),nrows=3071)

# Inspect the dataframe (optional/used for testing)
#print(postureData.head())

# Create and prepare datasets 
X = dfMocapData[['X2','Y2']]
Y = dfMocapData['Z2']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

# Create the Linear Regression Model
model = LinearRegression()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

# Print the coefficients
print('Coefficients:',model.coef_)
print('Intercept:',model.intercept_)

# Print R Sqaured 
r2 = model.score(X_test,Y_test)
print('R-Squared:',r2)

# Create the scatter plot
plt.scatter(Y_test,Y_pred)
plt.xlabel('Independent Variables: X and Y')
plt.ylabel('Predicted: Z ')
plt.title('Motion Capture Posture Data: User 2 Marker 3 Linear Regression')

# Show the Graph
plt.show() 
