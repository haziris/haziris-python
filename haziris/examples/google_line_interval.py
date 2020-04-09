import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['a', 100,  90, 110,  85,  96, 104, 120],
    ['b', 120,  95, 130,  90, 113, 124, 140],
    ['c', 130, 105, 140, 100, 117, 133, 139],
    ['d',  90,  85,  95,  85,  88,  92,  95],
    ['e',  70,  74,  63,  67,  69,  70,  72],
    ['f',  30,  39,  22,  21,  28,  34,  40],
    ['g',  80,  77,  83,  70,  77,  85,  90],
    ['h', 100,  90, 110,  85,  95, 102, 110]
  ],
  columns = ['name', 's1', 's2', 's3', 's4', 's5', 's6', 's7']
)

hz.google_line_chart(df, 
  "google_line_interval.html", 
  {'curveType':'function'}, 
  intervals =['s2', 's3', 's4', 's5', 's6', 's7']
)
