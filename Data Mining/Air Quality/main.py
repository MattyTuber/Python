import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality.csv", index_col=0, parse_dates=True)

air_quality.plot()
plt.show()

air_quality.plot().box()
plt.show()