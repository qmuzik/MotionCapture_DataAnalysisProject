# Final Project by Quincy Muzik 12//2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the CSV File with custom parameters
postureData = pd.read_csv(r'C:\Users\Quincy\Documents\UW Stout\Statistics for Engineers and Scientists\Final Project\Postures.csv',usecols=lambda x: x not in ["Class","User"])

# Step 2: Inspect the dataframe (optional/used for testing)
print(postureData.head())

# Step 3: Plot the data for User 1 Posture 1
postureData.plot()
plt.title('Motion Capture Hand Postures')
plt.xlabel('Frame Number')
plt.ylabel('Marker location in 3D Space')
plt.show()

