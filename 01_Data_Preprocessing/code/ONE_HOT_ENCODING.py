# =====================================================
# ONE HOT ENCODING
# =====================================================

import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "IT"]
})

encoded_df = pd.get_dummies(
    df,
    columns=["Department"]
)

print(encoded_df)

# Creates:
# Department_Finance
# Department_HR
# Department_IT