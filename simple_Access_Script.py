import pandas as pd
import matplotlib.pyplot as plt


# Get path of file 
file_Path = "Compiled Airplane Delays and Diversions Per Date per Year\compiled_arrival_and_departure_delays_2020.csv"

# Import dataset into a Pandas Dataframe
df = pd.read_csv(file_Path)
# Print head to verify that it was imported correctly
print(df.head())

# Plot as a Bar chart 
df.plot.bar(x = 'DATE', y = 'num_of_arrival_and_departure_delays', rot = 0)
plt.show()