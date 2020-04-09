import pandas as pd
import haziris as hz
import numpy as np

def dtm(days): #daysToMilliseconds
  return days * 24 * 60 * 60 * 1000

df = pd.DataFrame([
    ['Research', 'Find sources'       ,"2015-01-01 00:00:00", "2015-01-05 00:00:00", np.nan, 100, np.nan ],
    ['Write'   , 'Write paper'        , np.nan     , "2015-01-09 00:00:00", dtm(3),  25, 'Research,Outline'],
    ['Cite'    , 'Create bibliography', np.nan     , "2015-01-07 00:00:00", dtm(1),  20, 'Research'        ],
    ['Complete', 'Hand in paper'      , np.nan     , "2015-01-10 00:00:00", dtm(1),   0, 'Cite,Write'      ],
    ['Outline' , 'Outline paper'      , np.nan     , "2015-01-06 00:00:00", dtm(1), 100, 'Research'        ]
  ],
  columns = ['Task ID', 'Task Name', 'Start Date', 'End Date', 'Duration', 'Percent Complete', 'Dependencies'] 
)

hz.google_gantt_chart(df, "google_gantt.html")