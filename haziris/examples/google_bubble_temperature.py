import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['', 80, 167, 120],
    ['', 79, 136, 130],
    ['', 78, 184, 50],
    ['', 72, 278, 230],
    ['', 81, 200, 210],
    ['', 72, 170, 100],
    ['', 68, 477, 80]
  ],
  columns = ['ID', 'X', 'Y', 'Temperature'] 
)

options = {
  'colorAxis': {
    'colors': ['yellow', 'red']
  }
}

hz.google_bubble_chart(df, "google_bubble_temperature.html", options)
