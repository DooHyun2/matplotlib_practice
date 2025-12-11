import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 600

dop = rng.uniform(0.00, 0.20, n) # dopant fraction
density = rng.uniform(0.90, 1.00, n) # relative density
gb_frac = rng.uniform(0.00, 0.30, n) # grain boundary fraction
temp_c = rng.uniform(20, 80, n) # temperature in celsius
temp_k = temp_c + 273.15

# ノイズ
noise = rng.normal(0, 0.03, n)

# conductivity model
log_sigma = (
0.5 * dop +
2.0 * (density - 0.90) -
1.5 * gb_frac +
0.01 * (temp_c - 20) +
noise
)

sigma = np.exp(log_sigma)


df = pd.DataFrame({
"dop": dop,
"density": density,
"gb_frac": gb_frac,
"temp_c": temp_c,
"temp_k": temp_k,
"sigma": sigma
})

df.to_csv("synthetic_LLZO.csv", index=False)
print("saved synthetic_LLZO.csv", df.shape)
