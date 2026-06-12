# =====================================================
# LABEL ENCODING
# =====================================================
# note run all these codes in Google colab only 
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
})

le = LabelEncoder()

df["Department_Encoded"] = le.fit_transform(df["Department"])

print(df)


# output:   
# Finance -> 0
# HR      -> 1
# IT      -> 2