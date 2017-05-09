import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
data["total_enrollment"] = data["TOT_ENR_M"]+data["TOT_ENR_F"]

#Compute sum of all columns that break down enrollment by race and gender
cols = ["SCH_ENR_HI_M","SCH_ENR_HI_F","SCH_ENR_AM_M",
       "SCH_ENR_AM_F","SCH_ENR_AS_M","SCH_ENR_AS_F",
       "SCH_ENR_HP_M","SCH_ENR_HP_F","SCH_ENR_BL_M",
       "SCH_ENR_BL_F","SCH_ENR_WH_M","SCH_ENR_WH_F",
       "SCH_ENR_TR_M","SCH_ENR_TR_F"]

all_enrollment = sum(data["total_enrollment"])
print(all_enrollment)

sums = {}
pct_enrollment = {}
for i in cols:
    sums[i]=sum(data[i])
    pct_enrollment[i] = sums[i]/all_enrollment
    
print(sums)

print(pct_enrollment)