# ==========================================
# DATA
# ==========================================

X = [1, 2, 3, 4, 5]   # our data
y = [3, 5, 7, 9, 11]  # we have to predict this

# ==========================================
# MODEL PARAMETERS (randomly chosen)
# ==========================================

m = 2
c = 1

# ==========================================
# PREDICTIONS
# ==========================================

for x in X:
    prediction = m * x + c
    print(f"Input={x}  Prediction={prediction}")
    
# output :
# Input=1  Prediction=3
# Input=2  Prediction=5
# Input=3  Prediction=7
# Input=4  Prediction=9
# Input=5  Prediction=11