import pandas as pd
data=pd.read_csv("WSWP2.csv")
print(data.describe().transpose())


