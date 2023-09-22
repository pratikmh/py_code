import pandas as pd
data={"name":["pratik","hr","sachin"],
      "english":[76,87,65],
       "bio":[56,57,55],
        "math":[54,83,95]
      }
df=pd.DataFrame(data,index=[101,102,103])
print(df)
df["total marks"]=df["english"]+df["bio"]+df["math"]
df["percentage"]=round(df["total marks"]/4,2)
print(df)