import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("experiments_results.csv")

plt.figure(figsize=(8,5))
plt.bar(df["Model"], df["MAE"])
plt.title("Model Comparison (Lower is Better)")
plt.ylabel("MAE")
plt.show()
