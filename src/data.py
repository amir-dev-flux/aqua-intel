import pandas as pd

def load_data(path="data/riyadh_climate.csv"):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df
