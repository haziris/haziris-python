import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['George Washington', '1789-03-30 00:00:00', '1797-02-04 00:00:00' ],
    ['John Adams'       , '1797-02-04 00:00:00', '1801-02-04 00:00:00' ],
    ['Thomas Jefferson' , '1801-02-04 00:00:00', '1809-02-04 00:00:00' ]
  ],
  columns = ['President', 'Start', 'End']
)

hz.google_timeline_chart( df, "google_timeline.html" )
