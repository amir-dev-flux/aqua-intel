from src.data import load_data
from src.features import add_et0, add_lag_features
from src.model import train_model, evaluate

import pandas as pd

df = load_data()
df = add_et0(df)
df = add_lag_features(df)

df = df.dropna()

features = ["T2M", "RH2M", "WS2M", "ALLSKY_SFC_SW_DWN",
            "ET0_lag_1", "ET0_lag_3", "ET0_lag_7"]

X = df[features]
y = df["ET0"]

split = int(len(df)*0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = train_model(X_train, y_train)
mae, rmse, preds = evaluate(model, X_test, y_test)

print("MAE:", mae)
print("RMSE:", rmse)
