# Airplane-Delays-and-Diversions-Dataset
A dataset listing the amount of delays or diversions per day according to the USA Bureau of Transportation Statistics[1] for every year between January 1st 1990 and December 31st 2020

## Dataset Aim

This dataset was compiled by Paraskevas Solomou using data provided by the Bureau of Transportation Statistics, in order to encourage Statistics and Machine Learning related research. 

## Dataset Overview


The flight delay dataset used [1] was provided by the USA Bureau of Transportation Statistics (BTS) for Flight data. 
This dataset contains data documenting the performance of domestic flights operated by large air carriers.
During this project, all data entries from January 1st 1990 until December 31st 2020 were obtained and compiled in a user-friendly two-dimentional dataset.

BTS defines a delay as any flight which arrives or departs fifteen minutes earlier or later than the scheduled time [See FAQs below]. 
This dataset also lists the nuber of diversions between January 1st 1990 and December 31st 2020.

## Dataset Description

The present dataset consists of two features those being: 

- DATE         | date format (yyyy/mm/dd)
- number_of_delays | integer 

![Alt text](https://github.com/Paris778/Airplane-Delays-and-Diversions-Dataset/blob/main/Screenshots/Capture2.JPG "Example Data")
  

## Usage Example (Python 3)

##### 1. Download Dataset
##### 1.5. Set up a virtual environment (Anaconda / MiniConda for Python) 
  Tutorial: https://katiekodes.com/setup-python-windows-miniconda/

  ##### 2. Download Dependencies
  - pandas
  - matplotlib (Use for plotting graphs) 
``` bash
  pip3 install pandas
  pip3 install matplotlib
```
  
##### 3. Load dataset (exmple usage script)
```python
# Import dependencies
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
```
## 
##### Graphical Representation 1994
![Alt text](https://github.com/Paris778/Airplane-Delays-and-Diversions-Dataset/blob/main/Screenshots/Capture.JPG "Graph")

## FAQs 

https://www.bts.dot.gov/explore-topics-and-geography/topics/airline-time-performance-and-causes-flight-delays

#### References

[1] Anon, OST_R: BTS: Title from h2. BTS. Available at: https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp [Accessed May 23, 2021]. 

[2] https://www.bts.gov/topics/airlines-and-airports/understanding-reporting-causes-flight-delays-and-cancellations

[3] https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp
## License
[MIT](https://choosealicense.com/licenses/mit/)

