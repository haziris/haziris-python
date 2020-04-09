import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ["2012-03-13", 37032],
    ["2012-03-14", 38024],
    ["2012-03-15", 38024],
    ["2012-03-16", 38108],
    ["2012-03-17", 38229],
    ["2012-03-18", 37967],
    ["2012-03-20", 36770],
    ["2012-03-21", 37839],
    ["2012-03-30", 37359]
  ],
  columns = ['Date', 'Attendance']
)

options = {
  'colorAxis': {
    'colors': ['yellow', 'red']
  }
}

hz.google_calendar_chart(df, "google_calendar.html", options)
