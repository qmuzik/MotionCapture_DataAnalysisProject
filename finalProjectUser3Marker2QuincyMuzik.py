# Final Project User 3 Marker 2 by Quincy Muzik 12/9/2024

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV File with custom parameters
dfMocapData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv',nrows=1)

# Load the CSV with additional parameters 
dfMocapData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv', skiprows=range(2,8296),nrows=2727)

# Inspect the dataframe (optional/used for testing)
#print(postureData.head())

# Plot the data for Marker 1 X, Y, Z Position
plt.plot(dfMocapData['X1'],label='X-Position')
plt.plot(dfMocapData['Y1'], label='Y-Position')
plt.plot(dfMocapData['Z1'], label='Z-Position')
plt.legend()

# Create the Layout of the Graph
plt.title('Motion Capture Posture Data: User 3 Marker 2')
plt.xlabel('Frame Number')
plt.ylabel('Location in 3D Space')

# Show the Graph
plt.show() 
