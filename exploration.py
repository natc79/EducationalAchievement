import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
#look at value counts in these two columns
print(data["JJ"].value_counts())
print(data["SCH_STATUS_MAGNET"].value_counts())

#Create two pivot tables that aggregate tot_enr_m and 
print(pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum"))

print(pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum"))
