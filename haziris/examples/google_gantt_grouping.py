import pandas as pd
import haziris as hz
import numpy as np

def t(date):
  return date+' 00:00:00'

df = pd.DataFrame([
    ['2014Spring', 'Spring 2014'      , 'spring', t("2014-03-23"), t("2014-06-20"), 100],
    ['2014Summer', 'Summer 2014'      , 'summer', t("2014-06-22"), t("2014-09-20"), 100],
    ['2014Autumn', 'Autumn 2014'      , 'autumn', t("2014-09-22"), t("2014-12-20"), 100],
    ['2014Winter', 'Winter 2014'      , 'winter', t("2014-12-22"), t("2015-03-21"), 100],
    ['2015Spring', 'Spring 2015'      , 'spring', t("2015-03-23"), t("2015-06-20"),  50],
    ['2015Summer', 'Summer 2015'      , 'summer', t("2015-06-22"), t("2015-09-20"),   0],
    ['2015Autumn', 'Autumn 2015'      , 'autumn', t("2015-09-22"), t("2015-12-20"),   0],
    ['2015Winter', 'Winter 2015'      , 'winter', t("2015-12-22"), t("2016-03-21"),   0],
    ['Football'  , 'Football Season'  , 'sports', t("2014-09-05"), t("2015-02-01"), 100],
    ['Baseball'  , 'Baseball Season'  , 'sports', t("2015-03-31"), t("2015-10-20"),  14],
    ['Basketball', 'Basketball Season', 'sports', t("2014-10-29"), t("2015-06-20"),  86],
    ['Hockey'    , 'Hockey Season'    , 'sports', t("2014-10-09"), t("2015-06-21"),  89]
  ],
  columns = ['Task ID', 'Task Name', 'Resource', 'Start Date', 'End Date', 'Percent Complete'] 
)

hz.google_gantt_chart(df, "Google gantt - Grouping.html")