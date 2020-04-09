import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['A', 'X', 5],
    ['A', 'Y', 7],
    ['A', 'Z', 6],
    ['B', 'X', 2],
    ['B', 'Y', 9],
    ['B', 'Z', 4]
  ],
  columns = ['From', 'To', 'Weight']
)

hz.google_sankey_chart( df, "google_sankey.html" )
