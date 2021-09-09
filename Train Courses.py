import numpy as np  
import re  
import nltk  
from sklearn.datasets import load_files  
nltk.download('stopwords')  
import pickle  
import pandas as pd
from nltk.corpus import stopwords

df1 = pd.ExcelFile('E:\courses2.xlsx')
df2 = pd.ExcelFile('E:\course info.xlsx')
# df1.dropna(inplace = True)

# df1["Course Name"] = df1["Course Name"].astype(str)
# df1["Course Name"] = df1["Course Name"].str.split(" ", 1)
# df1["Course Name"].str.get(0)

# df1 = df1.iloc[[0]]

df = df1.parse("Sheet1")
# print(df)
i = 0
while i < 6:
    x = df['Course Name'][i]
    print(x) 
    i = i+1
    

# sub = df1['Course Name'].str.split(': ')
# for df in df1:
#     print(df)

# df3 = df1[df1['Course Name'].str.contains(sub)]
# print(df3)

# for df in df2:
#     if df