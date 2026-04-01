import pandas as pd

df= pd.read_excel("excel idea.xlsx")

d= df["Depth"][0]-50
Mu= df["Moment"][0]*1e6

R= Mu/(df["Width"][0]*d**2)

if R<4: 
   Ratio=0.0055
else:
   Ratio= 0.0065

As= Ratio *df["Width"][0]*d

df["As"]=As

df.to_csv("Result.csv",index=False)
print("As=",As)
print("Done")
hhhfhhhfh