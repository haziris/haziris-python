import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['2014', 1000,  400, 200],
    ['2015', 1170,  460, 250],
    ['2016',  660, 1120, 300],
    ['2017', 1030,  540, 350]
  ],
  columns = ['Year', 'Sales', 'Expenses', 'Profit']
)

hz.google_material_bar_chart(df, "google_material_bar.html", {'legned':'None'})
