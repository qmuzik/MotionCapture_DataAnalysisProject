# Final Project User 1 Marker 1 by Quincy Muzik 12/10/2024

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV File with custom parameters
dfMocapData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv',nrows=5225)

# Inspect the dataframe (optional/used for testing)
#print(postureData.head())

# Plot the data for Marker 1 X, Y, Z Position
plt.plot(dfMocapData['X0'],label='X-Position')
plt.plot(dfMocapData['Y0'], label='Y-Position')
plt.plot(dfMocapData['Z0'], label='Z-Position')
plt.legend()

# Create the Layout of the Graph
plt.title('Motion Capture Posture Data: User 1 Marker 1')
plt.xlabel('Frame Number')
plt.ylabel('Location in 3D Space')

# Show the Graph
plt.show() 
