import pandas as pd
df = pd.read_excel("excel idea.xlsx")

b= df["Width"][0]
h= df["Depth"][0]
fy= df["fy"][0]
fcu = df["fcu"][0]
Mu = df["Moment"][0]

cover = 50
d = h - cover

R = Mu / (b * d**2)

if R<4:
    ratio = 0.0055
else:
    ratio = 0.0065
As = ratio * b * d
df["As"] = As
df.to_csv("result.csv",index=False)
print("done! check result in csv file")   