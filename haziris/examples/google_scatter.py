import pandas as pd
import haziris as hz

df = pd.DataFrame([
    [  8, 12],
    [  4,  5],
    [ 11, 14],
    [  4,  5],
    [  3,  3],
    [  6,  7]
  ],
  columns = ['Age', 'Weight']
)

options = {
  'title': 'Age vs. Weight comparison',
  'hAxis': {'title': 'Age', 'minValue': 0, 'maxValue': 15},
  'vAxis': {'title': 'Weight', 'minValue': 0, 'maxValue': 15},
  'legend': 'none'
}

hz.google_scatter_chart( df, "google_scatter.html", options )
