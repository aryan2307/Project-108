import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics
df = pd.read_csv(r"C:/Users/Admin/Downloads/Project108/project108.csv")
rating = df["Avg Rating"].tolist()
fig = ff.create_distplot([rating], ["average rating"], show_hist=True)
fig.show()
print(statistics.mean(rating))
print(statistics.median(rating))
print(statistics.mode(rating))