import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['Work'    , 11],
    ['Eat'     ,  2],
    ['Commute' ,  2],
    ['Watch TV',  2],
    ['Sleep'   ,  7]
  ],
  columns = ['Task', 'Hours per Day']
)
options = { 'title': 'My Daily Activities', 'pieHole': 0.4 }

hz.google_pie_chart( df, "google_pie_donut.html", options )