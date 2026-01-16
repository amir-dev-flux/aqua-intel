import streamlit as st
import pandas as pd

from src.data import load_data
from src.features import add_et0, add_lag_features
from src.model import train_model
from src.predict import recommend_irrigation

# Train model once
df = load_data()
df = add_et0(df)
df = add_lag_features(df)
df = df.dropna()

features = ["T2M", "RH2M", "WS2M", "ALLSKY_SFC_SW_DWN",
            "ET0_lag_1", "ET0_lag_3", "ET0_lag_7"]

X = df[features]
y = df["ET0"]

model = train_model(X, y)

st.title("AQUA-INTEL 💧")
st.subheader("AI-Powered Irrigation Advisor (Saudi Focus)")

temp = st.slider("Temperature (°C)", 20, 55, 35)
rh = st.slider("Humidity (%)", 5, 100, 30)
wind = st.slider("Wind Speed (m/s)", 0, 15, 3)
solar = st.slider("Solar Radiation", 5, 40, 25)

crop = st.selectbox("Crop Type", ["date_palm", "wheat", "vegetables"])

latest = df.iloc[-1]

input_df = pd.DataFrame([{
    "T2M": temp,
    "RH2M": rh,
    "WS2M": wind,
    "ALLSKY_SFC_SW_DWN": solar,
    "ET0_lag_1": latest["ET0_lag_1"],
    "ET0_lag_3": latest["ET0_lag_3"],
    "ET0_lag_7": latest["ET0_lag_7"]
}])

pred_et0 = model.predict(input_df)[0]
water = recommend_irrigation(pred_et0, crop)

st.success(f"💧 Recommended irrigation: {water:.2f} mm/day")
