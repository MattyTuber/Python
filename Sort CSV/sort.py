# importing pandas package
import pandas as pd
  
# assign dataset
data = pd.read_csv("iata_codes.csv")                                       

# sort data frame
data.sort_values(["label"], axis=0, ascending=[True], inplace=True)

for i in range(len(data)):
    print(data.iloc[i]['value'] + "," + data.iloc[i]['label'])