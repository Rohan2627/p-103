import pandas as pd
import plotly.express as pe


data = pd.read_csv("project 103/data.csv")
fig = pe.scatter(data, x="date", y = "cases" , color = "country")
fig.show()