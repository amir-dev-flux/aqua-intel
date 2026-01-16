def add_et0(df):
    T = df["T2M"]
    RH = df["RH2M"]
    WS = df["WS2M"]
    SR = df["ALLSKY_SFC_SW_DWN"]

    df["ET0"] = (
        0.0023 * (T + 17.8) * (SR ** 0.5)
        + 0.1 * WS
        - 0.05 * RH
    )
    return df


def add_lag_features(df, col="ET0", lags=[1,3,7]):
    for lag in lags:
        df[f"{col}_lag_{lag}"] = df[col].shift(lag)
    return df
