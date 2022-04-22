import numpy as np
import pandas as pd

#filenames = ["TestData.txt"]
filenames = ["McGovern1.asc", "McGovern2.asc", "McGovern3.asc", "McGovern4.asc", "McGovern5.asc"]
columns = ["Date", "Time", "Lat", "Lon", "Magnitude", "Type"]

print("Reading in files...")

for filename in filenames:
    dataframe = pd.read_csv(filename, header = None, delim_whitespace=True, names=columns)



numPositiveC = 0
numNegativeC = 0
numPositiveG = 0
numNegativeG = 0
numCC = 0
numCG = 0

print("Calculating statistics...")

n = 0

while n < len(dataframe):
    if dataframe["Type"][n] == "C":
        numCC += 1
        if dataframe["Magnitude"][n] > 0:
            numPositiveC += 1
        elif dataframe["Magnitude"][n] < 0:
            numNegativeC += 1
    elif dataframe["Type"][n] == "G":
        numCG += 1
        if dataframe["Magnitude"][n] > 0:
            numPositiveG += 1
        elif dataframe["Magnitude"][n] < 0:
            numNegativeG += 1
    n+=1

print("Statistics done")
print("\n----------------\n")
print(f"Number of positive strikes CC is {numPositiveC}")
print(f"Percent positive CC {(numPositiveC/(numNegativeC+numPositiveC))*100}%")
print(f"Number of negative strikes CC is {numNegativeC}")
print(f"Percent negative CC {(numNegativeC/(numNegativeC+numPositiveC))*100}%")
print("\n----------------\n")
print(f"Number of positive strikes CG is {numPositiveG}")
print(f"Percent positive CG {(numPositiveG/(numNegativeG+numPositiveG))*100}%")
print(f"Number of negative strikes CG is {numNegativeG}")
print(f"Percent negative CG {(numNegativeG/(numNegativeG+numPositiveG))*100}%")
print("\n----------------\n")
print(f"Number of CC strikes {numCC}")
print(f"Percent CC {(numCC/(numCC+numCG))*100}%")
print(f"Number of CG strikes {numCG}")
print(f"Percent CG {(numCG/(numCC+numCG))*100}%")